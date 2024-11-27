from django.shortcuts import render
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from .forms import ResumeForm

def collect_resume_info(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            # Collect data from the form
            data = form.cleaned_data
            # Call the PDF generation function and pass all data from the form
            return generate_pdf(
                request,
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                skills=data['skills'],
                experience=data['experience'],
                education=data['education'],
                awards=data['awards'],
                references=data['references'],
                about_me=data['about_me']
            )
    else:
        form = ResumeForm()
    return render(request, 'builder/collect_resume_info.html', {'form': form})

def generate_pdf(request, name, email, phone, skills, experience, education, awards, references, about_me):
    # Prepare the data context for the template
    context = {
        'name': name,
        'email': email,
        'phone': phone,
        'skills': skills.split('\n'),  # Split skills into a list
        'experience': experience.split('\n'),  # Split experience into a list
        'education': education.split('\n'),  # Split education into a list
        'awards': awards.split('\n'),  # Split awards into a list
        'references': references.split('\n'),  # Split references into a list
        'about_me': about_me
    }

    # Render the HTML content with the data context
    html_string = render_to_string('builder/resume_template.html', context)

    # Create a PDF using WeasyPrint
    pdf_response = HttpResponse(content_type='application/pdf')
    pdf_response['Content-Disposition'] = 'attachment; filename="resume.pdf"'

    # Convert HTML to PDF
    HTML(string=html_string).write_pdf(pdf_response)

    return pdf_response
