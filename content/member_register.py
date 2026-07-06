import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import re
import glob


def create_directory(path):
    """
    Create directory if it doesn't exist
    """
    if not os.path.exists(path):
        os.makedirs(path)


def find_ja_en_directories(start_path=None):
    """
    Find the ja/en directories by searching from the start path
    If not found, ask the user to select the base directory
    """
    if start_path is None:
        start_path = os.getcwd()

    # Look for ja/en directories
    for root, dirs, _ in os.walk(start_path):
        if "ja" in dirs and "en" in dirs:
            ja_path = os.path.join(root, "ja")
            en_path = os.path.join(root, "en")

            # Verify if authors directory exists or can be created
            ja_authors = os.path.join(ja_path, "authors")
            en_authors = os.path.join(en_path, "authors")

            if (os.path.exists(ja_authors) or os.access(ja_path, os.W_OK)) and (
                os.path.exists(en_authors) or os.access(en_path, os.W_OK)
            ):
                return ja_path, en_path

    # If not found, ask user to select the root directory
    messagebox.showinfo(
        "ディレクトリ選択 / Directory Selection",
        "jaとenディレクトリが見つかりませんでした。\nプロジェクトのルートディレクトリを選択してください。\n\n"
        "Could not find ja and en directories.\nPlease select the project root directory.",
    )

    root_dir = filedialog.askdirectory(
        title="プロジェクトのルートディレクトリを選択 / Select Project Root Directory"
    )

    if not root_dir:
        return None, None

    # Check if ja/en directories exist in the selected directory
    ja_path = os.path.join(root_dir, "ja")
    en_path = os.path.join(root_dir, "en")

    # Create them if they don't exist
    if not os.path.exists(ja_path) or not os.path.exists(en_path):
        if messagebox.askyesno(
            "ディレクトリ作成 / Create Directories",
            "jaとenディレクトリが存在しません。作成しますか？\n\n"
            "ja and en directories do not exist. Create them?",
        ):
            if not os.path.exists(ja_path):
                os.makedirs(ja_path)
            if not os.path.exists(en_path):
                os.makedirs(en_path)
        else:
            return None, None

    # Create authors directories if they don't exist
    ja_authors = os.path.join(ja_path, "authors")
    en_authors = os.path.join(en_path, "authors")

    if not os.path.exists(ja_authors):
        os.makedirs(ja_authors)
    if not os.path.exists(en_authors):
        os.makedirs(en_authors)

    return ja_path, en_path


def find_profile_dirs(ja_base_path, en_base_path):
    """
    Find all profile directories in the ja/en paths
    """
    profiles = []
    ja_authors_path = os.path.join(ja_base_path, "authors")

    if os.path.exists(ja_authors_path):
        for author_dir in os.listdir(ja_authors_path):
            author_path = os.path.join(ja_authors_path, author_dir)
            if os.path.isdir(author_path) and os.path.exists(
                os.path.join(author_path, "_index.md")
            ):
                profiles.append(author_dir)

    return profiles


def parse_markdown_file(file_path):
    """
    Parse a markdown file and extract the yaml front matter
    """
    data = {}
    social_links = []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract YAML front matter
        match = re.search(r"---\s+(.*?)\s+---", content, re.DOTALL)
        if match:
            yaml_content = match.group(1)

            # Extract fields
            title_match = re.search(r"title:\s*(.*)", yaml_content)
            if title_match:
                data["title"] = title_match.group(1).strip()

            first_name_match = re.search(r"first_name:\s*(.*)", yaml_content)
            if first_name_match:
                data["first_name"] = first_name_match.group(1).strip()

            last_name_match = re.search(r"last_name:\s*(.*)", yaml_content)
            if last_name_match:
                data["last_name"] = last_name_match.group(1).strip()

            # 改良されたrole抽出 - コメントや余分なテキストを除去
            role_match = re.search(r"role:\s*(.*?)(?:\n\w|$)", yaml_content, re.DOTALL)
            if role_match:
                role_text = role_match.group(1).strip()
                # #で始まる行やコメントを除外
                if not role_text.startswith("#"):
                    # 複数行の場合は最初の行のみを使用
                    first_line = role_text.split("\n")[0]
                    data["role"] = first_line.strip()
                else:
                    data["role"] = ""
            else:
                data["role"] = ""

            user_group_match = re.search(r"user_groups:\s*\n-\s*(.*)", yaml_content)
            if user_group_match:
                data["user_group"] = user_group_match.group(1).strip()

            # Extract social links
            social_section = re.search(
                r"social:\s*(.*?)(?=\n\w)", yaml_content, re.DOTALL
            )
            if social_section:
                social_text = social_section.group(1)

                # GitHub
                github_match = re.search(
                    r"- icon: github.*?\n.*?link: (.*?)(?:\n|$)", social_text, re.DOTALL
                )
                if github_match and not github_match.group(1).startswith("#"):
                    social_links.append(("github", github_match.group(1).strip()))

                # Personal website
                website_match = re.search(
                    r"- icon: house.*?\n.*?link: (.*?)(?:\n|$)", social_text, re.DOTALL
                )
                if website_match and not website_match.group(1).startswith("#"):
                    social_links.append(("website", website_match.group(1).strip()))

                # Google Scholar
                scholar_match = re.search(
                    r"- icon: google-scholar.*?\n.*?link: (.*?)(?:\n|$)",
                    social_text,
                    re.DOTALL,
                )
                if scholar_match and not scholar_match.group(1).startswith("#"):
                    social_links.append(("scholar", scholar_match.group(1).strip()))

                # LinkedIn
                linkedin_match = re.search(
                    r"- icon: linkedin.*?\n.*?link: (.*?)(?:\n|$)",
                    social_text,
                    re.DOTALL,
                )
                if linkedin_match and not linkedin_match.group(1).startswith("#"):
                    social_links.append(("linkedin", linkedin_match.group(1).strip()))

            data["social_links"] = social_links

    except Exception as e:
        messagebox.showerror(
            "エラー / Error",
            f"マークダウンファイルの解析中にエラーが発生しました: {str(e)}",
        )
        return None

    return data


class ProfileManager:
    def __init__(self, master=None):
        # Find ja/en directories
        self.ja_base_path, self.en_base_path = find_ja_en_directories()

        if self.ja_base_path is None or self.en_base_path is None:
            messagebox.showerror(
                "エラー / Error",
                "jaとenディレクトリを見つけられませんでした。\nプログラムを終了します。\n\n"
                "Could not find or create ja and en directories.\nExiting program.",
            )
            if master:
                master.destroy()
            return

        # Initialize main window
        if master is None:
            self.root = tk.Tk()
            self.root.title("プロファイル管理ツール / Profile Manager")
            self.root.geometry("700x800")
        else:
            self.root = master

        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Create tab for new profile
        self.new_profile_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.new_profile_tab, text="新規作成 / New Profile")

        # Create tab for edit profile
        self.edit_profile_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.edit_profile_tab, text="編集 / Edit Profile")

        # Setup the new profile tab
        self.setup_new_profile_tab()

        # Setup the edit profile tab
        self.setup_edit_profile_tab()

        # Set editing mode flag
        self.editing_mode = False
        self.current_profile_dir = None
        self.existing_avatar_path = None

    def setup_new_profile_tab(self):
        """
        Setup the new profile tab with all necessary widgets
        """
        # Display detected paths
        path_frame = ttk.Frame(self.new_profile_tab, padding=5)
        path_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(
            path_frame,
            text="検出されたディレクトリ / Detected directories:",
            font=("", 10, "bold"),
        ).pack(anchor="w")
        ttk.Label(path_frame, text=f"Japanese (ja): {self.ja_base_path}").pack(
            anchor="w"
        )
        ttk.Label(path_frame, text=f"English (en): {self.en_base_path}").pack(
            anchor="w"
        )

        # Create main frame with scrollbar
        main_frame = ttk.Frame(self.new_profile_tab)
        main_frame.pack(fill="both", expand=True)

        # Add canvas and scrollbar
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Create frame
        frame = ttk.Frame(scrollable_frame, padding=20)
        frame.pack(fill="both", expand=True)

        # Name input fields (both Japanese and English)
        ttk.Label(frame, text="日本語名（Last Name）:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.last_name_ja_entry = ttk.Entry(frame, width=30)
        self.last_name_ja_entry.grid(row=0, column=1, sticky="w", pady=5)

        ttk.Label(frame, text="日本語名（First Name）:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.first_name_ja_entry = ttk.Entry(frame, width=30)
        self.first_name_ja_entry.grid(row=1, column=1, sticky="w", pady=5)

        ttk.Label(frame, text="英語名（Last Name）:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.last_name_en_entry = ttk.Entry(frame, width=30)
        self.last_name_en_entry.grid(row=2, column=1, sticky="w", pady=5)

        ttk.Label(frame, text="英語名（First Name）:").grid(
            row=3, column=0, sticky="w", pady=5
        )
        self.first_name_en_entry = ttk.Entry(frame, width=30)
        self.first_name_en_entry.grid(row=3, column=1, sticky="w", pady=5)

        ttk.Label(frame, text="役職（日本語） / Role (Japanese):").grid(
            row=4, column=0, sticky="w", pady=5
        )
        self.role_ja_entry = ttk.Entry(frame, width=30)
        self.role_ja_entry.grid(row=4, column=1, sticky="w", pady=5)

        ttk.Label(frame, text="役職（英語） / Role (English):").grid(
            row=5, column=0, sticky="w", pady=5
        )
        self.role_en_entry = ttk.Entry(frame, width=30)
        self.role_en_entry.grid(row=5, column=1, sticky="w", pady=5)

        # User group selection
        ttk.Label(frame, text="ユーザーグループ（日本語）:").grid(
            row=6, column=0, sticky="w", pady=5
        )
        self.user_group_ja_var = tk.StringVar(self.root)
        self.user_group_ja_options = [
            "博士後期課程",
            "博士前期課程2年",
            "博士前期課程1年",
            "学部4年",
            "スタッフ",
            "ポスドク研究員",
            "招へい教員・研究員",
            "特任研究員S",
            "訪問学生",
        ]
        self.user_group_ja_var.set(self.user_group_ja_options[2])  # Default to M1
        self.user_group_ja_menu = ttk.Combobox(
            frame,
            textvariable=self.user_group_ja_var,
            values=self.user_group_ja_options,
            width=27,
        )
        self.user_group_ja_menu.grid(row=6, column=1, sticky="w", pady=5)

        ttk.Label(frame, text="ユーザーグループ（英語）:").grid(
            row=7, column=0, sticky="w", pady=5
        )
        self.user_group_en_var = tk.StringVar(self.root)
        self.user_group_en_options = [
            "PhD Students",
            "Master Students (M2)",
            "Master Students (M1)",
            "Undergraduate Students (B4)",
            "Staff",
            "PostDocs",
            "Visiting Faculty / Researcher",
            "Project Researcher (S)",
            "Visiting Students",
        ]
        self.user_group_en_var.set(self.user_group_en_options[2])  # Default to M1
        self.user_group_en_menu = ttk.Combobox(
            frame,
            textvariable=self.user_group_en_var,
            values=self.user_group_en_options,
            width=27,
        )
        self.user_group_en_menu.grid(row=7, column=1, sticky="w", pady=5)

        # Ensure Japanese and English user groups stay in sync
        def sync_user_group_ja(*args):
            index = self.user_group_ja_options.index(self.user_group_ja_var.get())
            self.user_group_en_var.set(self.user_group_en_options[index])

        def sync_user_group_en(*args):
            index = self.user_group_en_options.index(self.user_group_en_var.get())
            self.user_group_ja_var.set(self.user_group_ja_options[index])

        self.user_group_ja_var.trace("w", sync_user_group_ja)
        self.user_group_en_var.trace("w", sync_user_group_en)

        # Social links section
        ttk.Label(
            frame, text="ソーシャルリンク / Social Links", font=("", 12, "bold")
        ).grid(row=8, column=0, columnspan=2, sticky="w", pady=(15, 5))

        # GitHub
        self.github_var = tk.BooleanVar(value=False)  # Default to False
        self.github_check = ttk.Checkbutton(
            frame, text="GitHub", variable=self.github_var
        )
        self.github_check.grid(row=9, column=0, sticky="w", pady=5)
        self.github_entry = ttk.Entry(frame, width=30)
        self.github_entry.insert(0, "https://github.com/")  # Keep placeholder
        self.github_entry.grid(row=9, column=1, sticky="w", pady=5)

        # Personal Website
        self.website_var = tk.BooleanVar(value=False)  # Default to False
        self.website_check = ttk.Checkbutton(
            frame, text="個人ウェブサイト / Personal Website", variable=self.website_var
        )
        self.website_check.grid(row=10, column=0, sticky="w", pady=5)
        self.website_entry = ttk.Entry(frame, width=30)
        self.website_entry.insert(0, "https://")  # Keep placeholder
        self.website_entry.grid(row=10, column=1, sticky="w", pady=5)

        # Google Scholar
        self.scholar_var = tk.BooleanVar(value=False)  # Default to False
        self.scholar_check = ttk.Checkbutton(
            frame, text="Google Scholar", variable=self.scholar_var
        )
        self.scholar_check.grid(row=11, column=0, sticky="w", pady=5)
        self.scholar_entry = ttk.Entry(frame, width=30)
        self.scholar_entry.insert(
            0, "https://scholar.google.com/citations?user="
        )  # Keep placeholder
        self.scholar_entry.grid(row=11, column=1, sticky="w", pady=5)

        # LinkedIn
        self.linkedin_var = tk.BooleanVar(value=False)  # Default to False
        self.linkedin_check = ttk.Checkbutton(
            frame, text="LinkedIn", variable=self.linkedin_var
        )
        self.linkedin_check.grid(row=12, column=0, sticky="w", pady=5)
        self.linkedin_entry = ttk.Entry(frame, width=30)
        self.linkedin_entry.insert(
            0, "https://www.linkedin.com/in/"
        )  # Keep placeholder
        self.linkedin_entry.grid(row=12, column=1, sticky="w", pady=5)

        # Image path storage
        self.avatar_path = tk.StringVar()

        def select_avatar():
            """
            Open file dialog to select avatar image
            """
            file_path = filedialog.askopenfilename(
                title="アバター画像を選択 / Select Avatar Image",
                filetypes=[("画像ファイル / Image Files", "*.jpg *.jpeg *.png")],
            )
            if file_path:
                self.avatar_path.set(file_path)
                self.avatar_label.config(
                    text=f"選択済み: {os.path.basename(file_path)}"
                )

        # Avatar selection
        ttk.Label(
            frame, text="アバター画像 / Avatar Image:", font=("", 12, "bold")
        ).grid(row=13, column=0, columnspan=2, sticky="w", pady=(15, 5))
        ttk.Label(frame, text="画像サイズは正方形推奨 / Square image recommended").grid(
            row=14, column=0, columnspan=2, sticky="w", pady=(0, 5)
        )
        avatar_button = ttk.Button(
            frame, text="画像を選択 / Select Image", command=select_avatar
        )
        avatar_button.grid(row=15, column=0, sticky="w", pady=5)
        self.avatar_label = ttk.Label(frame, text="未選択 / Not selected")
        self.avatar_label.grid(row=15, column=1, sticky="w", pady=5)

        # Generate button
        generate_button = ttk.Button(
            frame,
            text="マークダウンファイルを生成 / Generate Markdown Files",
            command=self.generate_files,
            style="Accent.TButton",
        )
        generate_button.grid(row=16, column=0, columnspan=2, pady=20)

        # Style for button
        style = ttk.Style()
        style.configure("Accent.TButton", font=("", 11, "bold"))

    def setup_edit_profile_tab(self):
        """
        Setup the edit profile tab with profile search and edit functionality
        """
        # Create frame for the edit tab
        edit_frame = ttk.Frame(self.edit_profile_tab, padding=20)
        edit_frame.pack(fill="both", expand=True)

        # Section for profile search
        ttk.Label(
            edit_frame, text="プロファイル検索 / Profile Search", font=("", 12, "bold")
        ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        # Search button
        search_button = ttk.Button(
            edit_frame,
            text="既存プロファイルを検索 / Search Existing Profiles",
            command=self.search_profiles,
        )
        search_button.grid(row=1, column=0, columnspan=2, sticky="w", pady=(0, 10))

        # Listbox to display found profiles
        ttk.Label(edit_frame, text="検索結果 / Search Results:").grid(
            row=2, column=0, sticky="w", pady=(10, 5)
        )

        self.profile_listbox_frame = ttk.Frame(edit_frame)
        self.profile_listbox_frame.grid(
            row=3, column=0, columnspan=2, sticky="nsew", pady=(0, 10)
        )

        # Configure grid to expand the listbox
        edit_frame.columnconfigure(0, weight=1)
        edit_frame.rowconfigure(3, weight=1)

        # Create scrollable listbox
        self.profile_listbox = tk.Listbox(
            self.profile_listbox_frame, height=10, width=60
        )
        scrollbar = ttk.Scrollbar(
            self.profile_listbox_frame,
            orient="vertical",
            command=self.profile_listbox.yview,
        )
        self.profile_listbox.configure(yscrollcommand=scrollbar.set)

        self.profile_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Double click to select a profile
        self.profile_listbox.bind("<Double-1>", self.load_selected_profile)

        # Buttons to load or delete the selected profile
        button_frame = ttk.Frame(edit_frame)
        button_frame.grid(row=4, column=0, columnspan=2, sticky="w", pady=(5, 20))

        load_button = ttk.Button(
            button_frame,
            text="選択したプロファイルを読み込む / Load Selected Profile",
            command=self.load_selected_profile,
        )
        load_button.pack(side="left", padx=(0, 10))

        delete_button = ttk.Button(
            button_frame,
            text="選択したプロファイルを削除 / Delete Selected Profile",
            command=self.delete_selected_profile,
        )
        delete_button.pack(side="left")

        # Instructions
        instructions = (
            "プロファイルを編集するには、上の「既存プロファイルを検索」ボタンをクリックし、\n"
            "リストから編集したいプロファイルを選択して「読み込む」ボタンをクリックしてください。\n\n"
            "To edit a profile, click the 'Search Existing Profiles' button above,\n"
            "select a profile from the list, and click the 'Load' button."
        )

        instruction_label = ttk.Label(edit_frame, text=instructions, justify="left")
        instruction_label.grid(row=5, column=0, columnspan=2, sticky="w", pady=(0, 10))

    def search_profiles(self):
        """
        Search for existing profile directories and display in the listbox
        """
        self.profile_listbox.delete(0, tk.END)

        profiles = find_profile_dirs(self.ja_base_path, self.en_base_path)

        if not profiles:
            messagebox.showinfo(
                "検索結果 / Search Result",
                "プロファイルが見つかりませんでした。\n\nNo profiles found.",
            )
            return

        # Sort profiles alphabetically
        profiles.sort()

        # Add profiles to the listbox
        for profile in profiles:
            self.profile_listbox.insert(tk.END, profile)

        messagebox.showinfo(
            "検索結果 / Search Result",
            f"{len(profiles)}件のプロファイルが見つかりました。\n\n"
            f"{len(profiles)} profiles found.",
        )

    def load_selected_profile(self, event=None):
        """
        Load the selected profile data into the form
        """
        selection = self.profile_listbox.curselection()

        if not selection:
            messagebox.showinfo(
                "選択エラー / Selection Error",
                "プロファイルを選択してください。\n\nPlease select a profile.",
            )
            return

        profile_dir = self.profile_listbox.get(selection[0])

        # Set the current profile directory
        self.current_profile_dir = profile_dir

        # Load ja profile
        ja_index_path = os.path.join(
            self.ja_base_path, "authors", profile_dir, "_index.md"
        )
        ja_data = parse_markdown_file(ja_index_path)

        # Load en profile
        en_index_path = os.path.join(
            self.en_base_path, "authors", profile_dir, "_index.md"
        )
        en_data = parse_markdown_file(en_index_path)

        if not ja_data or not en_data:
            messagebox.showerror(
                "読み込みエラー / Load Error",
                "プロファイルの読み込み中にエラーが発生しました。\n\n"
                "Error occurred while loading the profile.",
            )
            return

        # Set the form fields with the loaded data
        # Name fields
        self.first_name_ja_entry.delete(0, tk.END)
        self.first_name_ja_entry.insert(0, ja_data.get("first_name", ""))

        self.last_name_ja_entry.delete(0, tk.END)
        self.last_name_ja_entry.insert(0, ja_data.get("last_name", ""))

        self.first_name_en_entry.delete(0, tk.END)
        self.first_name_en_entry.insert(0, en_data.get("first_name", ""))

        self.last_name_en_entry.delete(0, tk.END)
        self.last_name_en_entry.insert(0, en_data.get("last_name", ""))

        # Role fields
        self.role_ja_entry.delete(0, tk.END)
        self.role_ja_entry.insert(0, ja_data.get("role", ""))

        self.role_en_entry.delete(0, tk.END)
        self.role_en_entry.insert(0, en_data.get("role", ""))

        # User group fields
        if ja_data.get("user_group") in self.user_group_ja_options:
            self.user_group_ja_var.set(ja_data.get("user_group"))

        if en_data.get("user_group") in self.user_group_en_options:
            self.user_group_en_var.set(en_data.get("user_group"))

        # Social links
        # Reset all checkboxes and entries
        self.github_var.set(False)
        self.website_var.set(False)
        self.scholar_var.set(False)
        self.linkedin_var.set(False)

        self.github_entry.delete(0, tk.END)
        self.github_entry.insert(0, "https://github.com/")

        self.website_entry.delete(0, tk.END)
        self.website_entry.insert(0, "https://")

        self.scholar_entry.delete(0, tk.END)
        self.scholar_entry.insert(0, "https://scholar.google.com/citations?user=")

        self.linkedin_entry.delete(0, tk.END)
        self.linkedin_entry.insert(0, "https://www.linkedin.com/in/")

        # Set social links from loaded data
        for social_type, link in ja_data.get("social_links", []):
            if social_type == "github":
                self.github_var.set(True)
                self.github_entry.delete(0, tk.END)
                self.github_entry.insert(0, link)
            elif social_type == "website":
                self.website_var.set(True)
                self.website_entry.delete(0, tk.END)
                self.website_entry.insert(0, link)
            elif social_type == "scholar":
                self.scholar_var.set(True)
                self.scholar_entry.delete(0, tk.END)
                self.scholar_entry.insert(0, link)
            elif social_type == "linkedin":
                self.linkedin_var.set(True)
                self.linkedin_entry.delete(0, tk.END)
                self.linkedin_entry.insert(0, link)

        # Check if avatar exists and set the path
        ja_avatar_path = os.path.join(
            self.ja_base_path, "authors", profile_dir, "avatar.jpg"
        )
        if os.path.exists(ja_avatar_path):
            self.avatar_path.set("")  # Clear the path initially
            self.existing_avatar_path = ja_avatar_path  # Store existing avatar path
            self.avatar_label.config(
                text=f"既存のアバター: avatar.jpg (更新する場合のみ再選択してください)"
            )
        else:
            self.avatar_path.set("")
            self.existing_avatar_path = None  # No existing avatar
            self.avatar_label.config(
                text="アバターなし: アバター画像を選択してください"
            )

        # Switch to the new profile tab for editing
        self.notebook.select(0)

        # Set editing mode
        self.editing_mode = True

        messagebox.showinfo(
            "プロファイル読み込み / Profile Loaded",
            f"プロファイル「{profile_dir}」を読み込みました。\n"
            "編集後に「マークダウンファイルを生成」ボタンをクリックして更新してください。\n\n"
            f"Profile '{profile_dir}' loaded.\n"
            "Edit as needed and click 'Generate Markdown Files' to update.",
        )

    def delete_selected_profile(self):
        """
        Delete the selected profile
        """
        selection = self.profile_listbox.curselection()

        if not selection:
            messagebox.showinfo(
                "選択エラー / Selection Error",
                "プロファイルを選択してください。\n\nPlease select a profile.",
            )
            return

        profile_dir = self.profile_listbox.get(selection[0])

        # Ask for confirmation
        confirm = messagebox.askyesno(
            "削除確認 / Confirm Deletion",
            f"プロファイル「{profile_dir}」を削除しますか？\nこの操作は元に戻せません。\n\n"
            f"Are you sure you want to delete the profile '{profile_dir}'?\nThis action cannot be undone.",
        )

        if not confirm:
            return

        # Delete the profile directories
        ja_profile_path = os.path.join(self.ja_base_path, "authors", profile_dir)
        en_profile_path = os.path.join(self.en_base_path, "authors", profile_dir)

        try:
            if os.path.exists(ja_profile_path):
                shutil.rmtree(ja_profile_path)

            if os.path.exists(en_profile_path):
                shutil.rmtree(en_profile_path)

            # Remove from listbox
            self.profile_listbox.delete(selection[0])

            messagebox.showinfo(
                "削除成功 / Deletion Successful",
                f"プロファイル「{profile_dir}」を削除しました。\n\n"
                f"Profile '{profile_dir}' has been deleted.",
            )
        except Exception as e:
            messagebox.showerror(
                "削除エラー / Deletion Error",
                f"プロファイルの削除中にエラーが発生しました: {str(e)}\n\n"
                f"Error occurred while deleting the profile: {str(e)}",
            )

    def generate_files(self):
        """
        Generate markdown files based on user input
        Either create a new profile or update an existing one
        """
        # Get English name for the directory structure
        first_en = self.first_name_en_entry.get().strip()
        last_en = self.last_name_en_entry.get().strip()

        # Get Japanese name for the content
        first_ja = self.first_name_ja_entry.get().strip()
        last_ja = self.last_name_ja_entry.get().strip()

        role_ja = self.role_ja_entry.get().strip()
        role_en = self.role_en_entry.get().strip()
        user_group_ja = self.user_group_ja_var.get()
        user_group_en = self.user_group_en_var.get()

        # Validate inputs
        if not first_ja or not last_ja:
            messagebox.showerror(
                "エラー / Error",
                "日本語名を入力してください / Please enter your Japanese name",
            )
            return

        if not first_en or not last_en:
            messagebox.showerror(
                "エラー / Error",
                "英語名を入力してください / Please enter your English name",
            )
            return

        # If not in editing mode, require an avatar image
        if not self.editing_mode and not self.avatar_path.get():
            messagebox.showerror(
                "エラー / Error",
                "アバター画像を選択してください / Please select an avatar image",
            )
            return

        # Create directory paths using lowercase English name
        first_lower = first_en.lower()
        last_lower = last_en.lower()
        dir_name = f"{first_lower}-{last_lower}"

        # Check if we're in editing mode and the name has changed
        if (
            self.editing_mode
            and self.current_profile_dir
            and self.current_profile_dir != dir_name
        ):
            # Confirm rename
            confirm = messagebox.askyesno(
                "名前変更確認 / Confirm Rename",
                f"プロファイルのディレクトリ名が変更されます: \n'{self.current_profile_dir}' → '{dir_name}'\n\n"
                "続行しますか？ (ファイルは新しい名前で作成され、古いファイルは残ります)\n\n"
                f"The profile directory name will change: \n'{self.current_profile_dir}' → '{dir_name}'\n\n"
                "Continue? (Files will be created with the new name, old files will remain)",
            )

            if not confirm:
                return

        ja_dir = os.path.join(self.ja_base_path, "authors", dir_name)
        en_dir = os.path.join(self.en_base_path, "authors", dir_name)

        create_directory(ja_dir)
        create_directory(en_dir)

        # Build social links section
        social_links_ja = []
        social_links_en = []

        if self.github_var.get():
            github_link = self.github_entry.get().strip()
            if github_link:
                social_links_ja.append(
                    f"- icon: github\n  icon_pack: fab\n  link: {github_link}"
                )
                social_links_en.append(
                    f"- icon: github\n  icon_pack: fab\n  link: {github_link}"
                )

        if self.website_var.get():
            website_link = self.website_entry.get().strip()
            if website_link:
                social_links_ja.append(
                    f"- icon: house\n  icon_pack: fas\n  link: {website_link}"
                )
                social_links_en.append(
                    f"- icon: house\n  icon_pack: fas\n  link: {website_link}"
                )

        if self.scholar_var.get():
            scholar_link = self.scholar_entry.get().strip()
            if scholar_link:
                social_links_ja.append(
                    f"- icon: google-scholar\n  icon_pack: fab\n  link: {scholar_link}"
                )
                social_links_en.append(
                    f"- icon: google-scholar\n  icon_pack: fab\n  link: {scholar_link}"
                )

        if self.linkedin_var.get():
            linkedin_link = self.linkedin_entry.get().strip()
            if linkedin_link:
                social_links_ja.append(
                    f"- icon: linkedin\n  icon_pack: fab\n  link: {linkedin_link}"
                )
                social_links_en.append(
                    f"- icon: linkedin\n  icon_pack: fab\n  link: {linkedin_link}"
                )

        # Join social links with newlines
        social_ja = (
            "\n".join(social_links_ja)
            if social_links_ja
            else "# - icon: github\n#  icon_pack: fab\n#  link: https://github.com/"
        )
        social_en = (
            "\n".join(social_links_en)
            if social_links_en
            else "# - icon: github\n#  icon_pack: fab\n#  link: https://github.com/"
        )

        # Create Japanese markdown file
        ja_content = f"""---
# Display name
title: {last_ja}{first_ja}
# Full Name (for SEO)
first_name: {first_ja}
last_name: {last_ja}
# Is this the primary user of the site?
#superuser: true
# Role/position
role: {role_ja}
# Social links
social:
{social_ja}
# - icon: envelope
#   icon_pack: fas
#   link: 'mailto:test@example.org'
# - icon: twitter
#   icon_pack: fab
#   link: https://twitter.com/GeorgeCushen
# Link to a PDF of your resume/CV from the About widget.
# To enable, copy your resume/CV to `static/files/cv.pdf` and uncomment the lines below.
# - icon: cv
#   icon_pack: ai
#   link: files/cv.pdf
# Enter email to display Gravatar (if Gravatar enabled in Config)
#email: ''
# Highlight the author in author lists? (true/false)
#highlight_name: false
# Organizational groups that you belong to (for People widget)
# Set this to `[]` or comment out if you are not using People widget.
user_groups:
- {user_group_ja}
---"""

        # Create English markdown file
        en_content = f"""---
# Display name
title: {first_en} {last_en}
# Full Name (for SEO)
first_name: {first_en}
last_name: {last_en}
# Is this the primary user of the site?
#superuser: true
# Role/position
role: {role_en}
# Social links
social:
{social_en}
# - icon: envelope
#   icon_pack: fas
#   link: 'mailto:test@example.org'
# - icon: twitter
#   icon_pack: fab
#   link: https://twitter.com/GeorgeCushen
# Link to a PDF of your resume/CV from the About widget.
# To enable, copy your resume/CV to `static/files/cv.pdf` and uncomment the lines below.
# - icon: cv
#   icon_pack: ai
#   link: files/cv.pdf
# Enter email to display Gravatar (if Gravatar enabled in Config)
#email: ''
# Highlight the author in author lists? (true/false)
#highlight_name: false
# Organizational groups that you belong to (for People widget)
# Set this to `[]` or comment out if you are not using People widget.
user_groups:
- {user_group_en}
---"""

        # Write markdown files
        with open(os.path.join(ja_dir, "_index.md"), "w", encoding="utf-8") as f:
            f.write(ja_content)

        with open(os.path.join(en_dir, "_index.md"), "w", encoding="utf-8") as f:
            f.write(en_content)

        # アバター画像の処理
        ja_avatar_dest = os.path.join(ja_dir, "avatar.jpg")
        en_avatar_dest = os.path.join(en_dir, "avatar.jpg")

        # Handle avatar image - either copy new or keep existing
        avatar_updated = False

        # 新しい画像が選択された場合
        if self.avatar_path.get():
            # Copy avatar image
            avatar_src = self.avatar_path.get()

            # Check if source file exists
            if not os.path.exists(avatar_src):
                messagebox.showerror(
                    "エラー / Error",
                    f"アバター画像ファイルが見つかりません: {avatar_src}\n\n"
                    f"Avatar image file not found: {avatar_src}\n\n"
                    "別の画像を選択してください。 / Please select another image.",
                )
                return

            # Try to copy or convert image to jpg
            try:
                # Remove existing files first to avoid potential locking issues
                if os.path.exists(ja_avatar_dest):
                    os.remove(ja_avatar_dest)
                if os.path.exists(en_avatar_dest):
                    os.remove(en_avatar_dest)

                shutil.copy2(avatar_src, ja_avatar_dest)
                shutil.copy2(avatar_src, en_avatar_dest)
                avatar_updated = True

                # Verify that files were created
                if not os.path.exists(ja_avatar_dest) or not os.path.exists(
                    en_avatar_dest
                ):
                    messagebox.showerror(
                        "エラー / Error",
                        "コピー後にアバター画像ファイルが見つかりません。\n"
                        "ディスク容量や権限を確認してください。\n\n"
                        "Avatar image file not found after copying.\n"
                        "Please check disk space or permissions.",
                    )
                    return

            except FileNotFoundError as e:
                messagebox.showerror(
                    "エラー / Error",
                    f"画像のコピー中にファイルが見つかりませんでした: {str(e)}\n\n"
                    f"File not found while copying image: {str(e)}\n\n"
                    "指定したファイルが存在するか確認してください。\n"
                    "Please verify that the specified file exists.",
                )
                return
            except PermissionError as e:
                messagebox.showerror(
                    "エラー / Error",
                    f"画像のコピー中にアクセス権限エラーが発生しました: {str(e)}\n\n"
                    f"Permission error while copying image: {str(e)}\n\n"
                    "ファイルへのアクセス権限があるか確認してください。\n"
                    "Please check if you have access permissions to the file.",
                )
                return
            except OSError as e:  # Catch potential OS errors like permission denied
                messagebox.showerror(
                    "エラー / Error",
                    f"画像のコピー中にOSエラーが発生しました: {str(e)}\n\n"
                    f"OS error while copying image: {str(e)}\n\n"
                    f"ファイルが他のプログラムで使用されていないか確認してください。\n"
                    f"Please ensure the file is not in use by another program.",
                )
                return
            except Exception as e:
                messagebox.showerror(
                    "エラー / Error",
                    f"画像のコピー中に予期せぬエラーが発生しました: {str(e)}\n\n"
                    f"Unexpected error while copying image: {str(e)}",
                )
                return
        # 編集モードで既存のアバターがある場合
        elif self.editing_mode and self.existing_avatar_path:
            # 既存のプロファイルと同じディレクトリ名の場合は画像コピーをスキップ
            if self.current_profile_dir == dir_name:
                # ディレクトリが変わらない場合は既存画像を維持
                pass
            else:
                # 名前が変更された場合は既存画像を新しいディレクトリにコピー
                try:
                    shutil.copy2(self.existing_avatar_path, ja_avatar_dest)
                    shutil.copy2(self.existing_avatar_path, en_avatar_dest)
                    avatar_updated = True
                except Exception as e:
                    messagebox.showerror(
                        "エラー / Error",
                        f"既存のアバター画像のコピー中にエラーが発生しました: {str(e)}\n\n"
                        f"Error occurred while copying existing avatar image: {str(e)}",
                    )
                    return

        # Operation message
        operation = "更新" if self.editing_mode else "作成"
        operation_en = "updated" if self.editing_mode else "created"

        avatar_msg = ""
        if avatar_updated:
            avatar_msg = "とアバター画像"
            avatar_msg_en = "and avatar image"
        else:
            avatar_msg = ""
            avatar_msg_en = ""

        messagebox.showinfo(
            "成功 / Success",
            f"マークダウンファイル{avatar_msg}が{operation}されました。\n\n"
            f"Markdown files {avatar_msg_en} have been {operation_en}.\n\n"
            f"Japanese: {ja_dir}\nEnglish: {en_dir}",
        )

        # Reset editing mode and current profile
        self.editing_mode = False
        self.current_profile_dir = None
        self.existing_avatar_path = None

        # Switch to edit tab and refresh the list
        self.notebook.select(1)
        self.search_profiles()

    def run(self):
        """
        Run the main application loop
        """
        if hasattr(self, "root"):
            self.root.mainloop()


def generate_markdown_files():
    """
    Main function to start the profile manager
    """
    app = ProfileManager()
    app.run()


if __name__ == "__main__":
    generate_markdown_files()
