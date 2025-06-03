# Project Initialization Script

## How to Use This File

1. **Initial Setup**
   - Copy this file to your new project directory
   - Open the file in Windsurf
   - Tell Windsurf: "Please execute the commands in this file to set up my new project"

2. **Customization**
   - Replace all placeholders (like `my-new-project`) with your actual project name
   - Update the template paths to point to your template repository
   - Review and customize the configuration as needed

3. **Execution**
   - The script is designed to be executed sequentially from top to bottom
   - Each section is clearly marked with a header and description
   - Commands are in code blocks for easy execution

---

This document contains a series of commands to be executed within Windsurf to set up a new project. Each section is designed to be executed sequentially.

## 1. Project Setup

```
# Create a new project directory and initialize git
mkdir my-new-project
cd my-new-project
git init
```

## 2. Create Project Structure

```
# Create all necessary directories
mkdir -p my-new-project/plans/{0_backlog,1_planning,2_inprogress,3_completed,_reference,_templates}
mkdir -p my-new-project/src/{css,js,views}
mkdir -p my-new-project/static/images

# Create empty content directory (will be populated with template files)
mkdir -p my-new-project/content

# Create essential files
touch my-new-project/README.md
touch my-new-project/index.html

# Verify directory structure
echo "Project structure created successfully!"
tree -L 2 my-new-project
```

## 3. Set Up Version Control

```
# Initialize git repository
cd my-new-project
git init

# Create initial commit
git add .
git commit -m "Initial commit: Project structure setup"

# Create and switch to development branch
git checkout -b develop
```

## 4. Copy Template Files

```
# Copy template files from templates directory
cp -r /path/to/templates/* my-new-project/

# Verify files were copied
echo "Template files copied successfully!"
```

## 5. Initialize Project

```
# Navigate to project directory
cd my-new-project

# Install dependencies (if applicable)
npm install  # or yarn install

# Build project (if applicable)
npm run build  # or yarn build

echo "Project initialization complete!"
```

## Project Structure

```
my-new-project/
├── plans/                    # Project management documents
│   ├── 0_backlog/           # Future features and ideas
│   ├── 1_planning/          # Active planning documents
│   ├── 2_inprogress/        # Work in progress
│   ├── 3_completed/         # Completed work
│   ├── _reference/          # Reference materials
│   └── _templates/          # Document templates
├── src/                     # Source code
│   ├── css/                 # Stylesheets
│   ├── js/                  # JavaScript files
│   └── views/               # View templates
├── static/                  # Static assets
│   └── images/              # Image files
├── content/                 # Content files
├── README.md                # Project documentation
└── index.html               # Main HTML file
```

## Next Steps

1. Update the README.md with project-specific information
2. Configure any necessary project settings
3. Start developing your project!

## Troubleshooting

- If you encounter permission issues, try running commands with `sudo`
- Make sure all required dependencies are installed
- Check file paths if you get "file not found" errors

## Support

For help with this template, please contact [Your Support Contact].
