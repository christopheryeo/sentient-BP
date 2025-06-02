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

## 3. Copy Template Files

```
# Set the path to the sentient-BP template repository
TEMPLATE_REPO="/Users/chrisyeo/Library/CloudStorage/OneDrive-Personal/Dev/windsurf/sentient-BP"

# Copy essential files
cp "$TEMPLATE_REPO/README.md" my-new-project/
cp "$TEMPLATE_REPO/index.html" my-new-project/

# Copy content files
cp "$TEMPLATE_REPO/content/"* my-new-project/content/

# Copy static assets
cp -r "$TEMPLATE_REPO/static/"* my-new-project/static/

# Copy plan templates and structure
mkdir -p my-new-project/plans/_templates
mkdir -p my-new-project/plans/_reference

# Copy templates, excluding specific files
cp -r "$TEMPLATE_REPO/plans/_templates/"* my-new-project/plans/_templates/

# Copy reference files, excluding CHANGELOG.md and ROADMAP.md
find "$TEMPLATE_REPO/plans/_reference/" -maxdepth 1 -type f ! -name 'CHANGELOG.md' ! -name 'ROADMAP.md' -exec cp {} my-new-project/plans/_reference/ \;

# Initialize CHANGELOG.md from template
cp "$TEMPLATE_REPO/plans/_templates/CHANGELOG_TEMPLATE.md" my-new-project/plans/_reference/CHANGELOG.md

# Initialize ROADMAP.md if template exists
if [ -f "$TEMPLATE_REPO/plans/_templates/ROADMAP_TEMPLATE.md" ]; then
    cp "$TEMPLATE_REPO/plans/_templates/ROADMAP_TEMPLATE.md" my-new-project/plans/_reference/ROADMAP.md
else
    touch my-new-project/plans/_reference/ROADMAP.md
fi

# Create plan directory structure
mkdir -p my-new-project/plans/{0_backlog,1_planning,2_inprogress,3_completed}

# Copy backlog files
cp "$TEMPLATE_REPO/plans/0_backlog/"*.md my-new-project/plans/0_backlog/

# Create empty planning and in-progress directories for future use
touch my-new-project/plans/1_planning/.gitkeep
touch my-new-project/plans/2_inprogress/.gitkeep
touch my-new-project/plans/3_completed/.gitkeep

# Copy source files
cp -r "$TEMPLATE_REPO/src/"* my-new-project/src/

# Verify files were copied
echo "\nCopied template files. Verifying..."
find my-new-project -type f | sort
```

## 4. Initialize Git Repository

```
# Navigate to project directory
cd my-new-project

# Initialize git repository
git init

# Create initial commit
git add .
git commit -m "Initial commit: Project setup with template structure"

# Verify git status
git status
```

## 5. Verify Project Setup

```
# Check directory structure
echo "\n=== Project Structure ==="
tree -L 2

# Verify essential files exist
echo "\n=== Essential Files ==="
ls -la
ls -la content/
ls -la plans/

# Verify git repository
echo "\n=== Git Status ==="
git status

echo "\nProject setup complete! Review the output above to ensure everything was created correctly."
```

## 6. Next Steps

1. Update the following files with your project-specific information:
   - `README.md`
   - `content/content.md`
   - Update any configuration files in the project

2. Review and update the following paths in the project:
   - Update image paths in HTML/CSS files
   - Update API endpoints if applicable
   - Update any hardcoded references to the template project

3. Run initial tests:
   - Open `index.html` in a browser to verify the presentation loads
   - Check console for any errors
   - Verify all images and assets load correctly

## Overview
[Brief project description]

## Getting Started
[Setup instructions]

## Project Structure
- `/plans` - Project management documents
- `/content` - Core presentation content
- `/static` - Static assets (images, styles, etc.)
EOL

# Create a basic .gitignore
cat > my-new-project/.gitignore << 'EOL'
# Dependencies
node_modules/
__pycache__/

# Environment variables
.env

# Build outputs
dist/
build/

# Logs
logs
*.log

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
Thumbs.db
EOL
```

## 4. Initialize Project Dependencies

```
# Initialize package.json (for Node.js projects)
cd my-new-project
npm init -y

# Or requirements.txt (for Python projects)
cat > requirements.txt << 'EOL'
# Add your Python dependencies here
# Example:
# flask==2.0.1
# pandas==1.3.3
EOL
```

## 5. Initialize Git Repository

```
# Initialize git repository
cd my-new-project
git add .
git commit -m "Initial commit: Project setup"
```

## 6. Create First Commit

```
# Add all files and make initial commit
git add .
git commit -m "Initial project setup with template structure"
```

## 7. Update Project Configuration

```
# Update project name in package.json (for Node.js)
sed -i '' 's/"name": "template"/"name": "my-new-project"/g' package.json

# Or update setup.py (for Python)
sed -i '' 's/name="template"/name="my-new-project"/g' setup.py
```

## 8. Verify Directory Structure

```
# Verify the directory structure was copied correctly
tree my-new-project -L 2

# Expected output:
# my-new-project/
# ├── README.md
# ├── .gitignore
# ├── content/
# ├── plans/
# └── static/
```

## 9. Create Initial Version Tag

```
# Create initial version tag
git tag -a v0.0.1 -m "Initial version"
```

## 10. Push to Remote Repository (Optional)

```
# Add remote repository
git remote add origin [repository-url]

# Push to main branch
git push -u origin main

# Push tags
git push --tags
```

## Usage Notes

1. Replace `/path/to/template-repo/` with the actual path to your template repository
2. Update placeholders (like project name, description) with actual values
3. Customize the .gitignore file based on your project's technology stack
4. Add any additional setup steps specific to your project's requirements
