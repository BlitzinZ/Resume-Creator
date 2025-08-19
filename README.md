
# Flask Resume Generator

A web-based application that allows users to create professional resumes by filling out a form and instantly generating a PDF document. Built with Flask and featuring multiple resume templates.

## 🚀 Features

- **Dynamic Template System**: Multiple professional resume templates to choose from
- **Comprehensive Data Collection**: Personal info, skills, experience, and photo upload
- **Real-time PDF Generation**: Instant conversion from form data to professional PDF
- **Photo Upload Support**: Add profile pictures to your resume
- **Secure File Handling**: Safe file upload with proper sanitization
- **Professional Formatting**: Print-ready, ATS-friendly resume layouts
- **In-browser Preview**: View your resume before downloading

## 🛠️ Technologies Used

### Backend
- **Flask** - Python web framework
- **Python 3.x** - Core programming language
- **pdfkit** - HTML to PDF conversion
- **Werkzeug** - Secure file handling

### Frontend
- **Jinja2** - Template engine
- **HTML5/CSS3** - Resume templates
- **Responsive Design** - Mobile-friendly layouts

### Dependencies
- **wkhtmltopdf** - PDF generation engine (system dependency)

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- wkhtmltopdf (system installation required)

### Step 1: Install wkhtmltopdf
**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install wkhtmltopdf
```

**macOS:**
```bash
brew install wkhtmltopdf
```

**Windows:**
Download from [wkhtmltopdf official website](https://wkhtmltopdf.org/downloads.html)

### Step 2: Clone the Repository
```bash
git clone https://github.com/yourusername/flask-resume-generator.git
cd flask-resume-generator
```

### Step 3: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 4: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Create Upload Directory
```bash
mkdir static/uploads
```

## 🔧 Configuration

Create a `.env` file in the project root:
```env
UPLOAD_FOLDER=static/uploads
MAX_CONTENT_LENGTH=16777216  # 16MB max file size
SECRET_KEY=your-secret-key-here
```

## 🚦 Usage

### Running the Application
```bash
python main.py
```

The application will be available at `http://localhost:5000`

### Creating a Resume
1. **Choose Template**: Select from available resume templates
2. **Fill Form**: Enter your personal information, skills, and experience
3. **Upload Photo**: (Optional) Add a professional headshot
4. **Generate PDF**: Click submit to create your resume
5. **Download**: Your PDF will be generated and ready for download

### Adding Experience Entries
The form supports multiple work experience entries:
- **Position**: Job title or role
- **Employer**: Company name
- **Dates**: Employment period
- **Skills**: Relevant skills for this position
- **Summary**: Detailed job description (supports multi-line text)

## 📁 Project Structure

```
flask-resume-generator/
├── main.py                 # Main Flask application
├── templates/              # Jinja2 templates
│   ├── template1.html      # Modern blue template
│   ├── template2.html      # Professional dark sidebar
│   └── form.html           # Resume input form
├── static/                # Static files
│   ├── css/              # Stylesheets
│   └── js/               # JavaScript files
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables
└── README.md            # This file
```

## 🎨 Available Templates

### Template 1 - Modern Blue Design
- Blue gradient header with diagonal design
- Two-column layout
- Clean typography with modern styling
- Photo integration with circular crop

### Template 2 - Professional Dark Sidebar
- Dark grey sidebar with white content area
- Structured sections with clear hierarchy
- Minimalist design with blue accents
- Perfect for business and sales roles

## 🔒 Security Features

- **Secure File Upload**: Filename sanitization using Werkzeug
- **File Type Validation**: Only allows image uploads for photos
- **Path Protection**: Secure file storage in designated upload directory
- **Session Management**: Template preferences stored securely

## 📋 Requirements.txt

```
Flask==2.3.3
pdfkit==1.0.0
Werkzeug==2.3.7
Jinja2==3.1.2
```

## 🚨 Troubleshooting

### Common Issues

**PDF Generation Fails:**
- Ensure wkhtmltopdf is properly installed
- Check if the upload folder exists and has write permissions
- Verify all form fields are filled correctly

**File Upload Issues:**
- Check file permissions on upload directory
- Ensure uploaded file is an image format
- Verify file size is within limits

**Template Not Found:**
- Ensure template files exist in the templates directory
- Check template name in session matches available templates

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-template`)
3. Commit your changes (`git commit -am 'Add new resume template'`)
4. Push to the branch (`git push origin feature/new-template`)
5. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Flask community for the excellent web framework
- wkhtmltopdf developers for the PDF generation engine
- Contributors who have helped improve this project

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the Flask documentation for additional help

---

**Made with ❤️ and Python**
