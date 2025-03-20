import os
import re
import shutil

# Paths
posts_dir = "/home/mafabrito/Portefolio/content"
attachments_dir = "/mnt/c/Users/mafas/iCloudDrive/iCloud~md~obsidian/Fabric/attachments"
static_images_dir = "/home/mafabrito/Portefolio/static/images/"

# Step 1: Process each markdown file in the posts directory and subdirectories
for root, _, files in os.walk(posts_dir):
    for filename in files:
        if filename.endswith(".md"):
            filepath = os.path.join(root, filename)
            
            with open(filepath, "r") as file:
                content = file.read()
            
            # Step 2: Find all image links with .png, .jpg, or .jpeg extensions
            images = re.findall(r'\[\[([^]]*\.(?:png|jpg|jpeg))\]\]', content, re.IGNORECASE)
            
            # Step 3: Replace image links and ensure URLs are correctly formatted
            for image in images:
                # Prepare the Markdown-compatible link with %20 replacing spaces
                markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
                content = content.replace(f"[[{image}]]", markdown_image)
                
                # Step 4: Copy the image to the Hugo static/images directory if it exists
                image_source = os.path.join(attachments_dir, image)
                if os.path.exists(image_source):
                    shutil.copy(image_source, static_images_dir)

            # Step 5: Write the updated content back to the markdown file
            with open(filepath, "w") as file:
                file.write(content)

print("Markdown files processed and images copied successfully.")
