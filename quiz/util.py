from quiz.models import Question


# http://stackoverflow.com/a/4581997
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_published_questions():
    return Question.objects.filter(state='PUB')


def save_data_in_session(data, session):
    session.modified = True

    for key, value in data.items():
        session[key] = value

    session.set_expiry(60 * 60 * 24 * 365 * 10)
