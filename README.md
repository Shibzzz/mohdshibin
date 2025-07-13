# My Jekyll Portfolio

This is a Jekyll-based portfolio project designed to showcase my work and skills. Below are the instructions for setting up and using the project.

## Project Structure

The project consists of the following key files and directories:

- **_includes/**: Contains reusable HTML snippets, such as the header.
- **_layouts/**: Contains layout templates for the site.
- **_posts/**: Contains blog posts written in Markdown format.
- **assets/**: Contains static assets like CSS files.
- **index.md**: The homepage of the portfolio.
- **_config.yml**: Configuration settings for the Jekyll site.
- **README.md**: This documentation file.

## Setup Instructions

1. **Install Jekyll**: Make sure you have Ruby and Bundler installed. Then, install Jekyll by running:
   ```
   gem install jekyll bundler
   ```

2. **Clone the Repository**: Clone this repository to your local machine:
   ```
   git clone <repository-url>
   cd my-jekyll-portfolio
   ```

3. **Install Dependencies**: Navigate to the project directory and install the required gems:
   ```
   bundle install
   ```

4. **Run the Jekyll Server**: Start the Jekyll server to view your site locally:
   ```
   bundle exec jekyll serve
   ```
   Your site will be available at `http://localhost:4000`.

## Usage Guidelines

- **Adding Posts**: To add a new blog post, create a new Markdown file in the `_posts/` directory following the naming convention `YYYY-MM-DD-title.md`.
- **Updating Styles**: Modify the CSS in `assets/css/style.css` to implement modern styling updates. Ensure that this file is linked in the `_layouts/default.html` file.
- **Customizing Configuration**: Update `_config.yml` to change the site title, description, and other metadata.

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.