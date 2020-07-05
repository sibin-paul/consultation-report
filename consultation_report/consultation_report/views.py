from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from datetime import timedelta
from django.views.generic import View
from consultation_report.utils import render_to_pdf
from django.template.loader import get_template
import socket
from datetime import date


def consultation_report(request):
	if request.method == 'GET':
		return render(request, 'consultation_report.html')
	if request.method == 'POST':
		hostname = socket.gethostname()
		ip_address = socket.gethostbyname(hostname)
		today = date.today()
		record = {}
		record['patient_firstname'] = request.POST["patient_firstname"]
		record['patient_lastname'] = request.POST["patient_lastname"]
		record['patient_dob'] = request.POST["patient_dob"]
		template = get_template('report.html')
		context = {
            "clinic_name": request.POST["clinic_name"],
            "physician_name": request.POST["physician_name"],
            "physician_contact": request.POST["physician_contact"],
            "patient_firstname": request.POST["patient_firstname"],
            "patient_lastname": request.POST["patient_lastname"],
            "patient_contact": request.POST["patient_contact"],
            "chief_complaint": request.POST["chief_complaint"],
            "consultation_note": request.POST.get('consultation_note', False),
            "ip_address": ip_address,
            "time_stamp": today,
        }
		html = template.render(context)
		pdf = render_to_pdf('report.html', context)
		if pdf:
			print("inside pdf")
			response = HttpResponse(pdf, content_type='application/pdf')
			filename = "CR_%s_%s_%s.pdf" %(record['patient_firstname'], record['patient_lastname'], record['patient_dob'])
			content = "inline; filename='%s'" %(filename)
			content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response



