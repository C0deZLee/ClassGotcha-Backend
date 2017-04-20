from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.core.mail import send_mail, EmailMessage

# def index(request):
#     return render(request, 'index.html')

@api_view(['POST'])
def test(request):
    if not request.user.is_superuser:
        return Response({'error': "BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        if request.POST['request']:
            send_email("subject",
            render_to_string("confirmation.html"),
            "team@classgotcha.com",
            ["yutse.lin0+test@gmail.com"])
            return Response({'message': "The email has been sent. "},  status=status.HTTP_201_CREATED)

        try:
            subject = request.POST['subject']
            message = request.POST['message']
            from_email = request.POST['from']
            html_message = bool(request.POST.get('html-message', False))
            recipient_list = [request.POST['to']]

            email = EmailMessage(subject, message, from_email, recipient_list)
            if html_message:
                email.content_subtype = 'html'
            email.send()
        except KeyError:
            return Response({'error': "KEY_ERROR"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({'message': "The email has been sent. "}, status=status.HTTP_201_CREATED)
    else:
        return Response({'error': "BAD_REQUEST"}, status=status.HTTP_400_BAD_REQUEST)


def send_email(subject, message, from_email, to_emails):
    email = EmailMessage(subject, message, from_email, to_emails)
    email.content_subtype = 'html'
    email.send()
