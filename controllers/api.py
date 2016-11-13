import tempfile

def index():
    pass

def get_user_name_from_email(email):
    """Returns a string corresponding to the user first and last names,
    given the user email."""
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])

def pretty_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    from datetime import datetime
    now = datetime.utcnow()
    if type(time) is int:
        diff = now - datetime.fromtimestamp(time)
    elif isinstance(time, datetime):
        diff = now - time
    elif not time:
        diff = now - now
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            logger.info("HEREEEEEEE")
            return "just now"
        if second_diff < 60:
            return str(second_diff) + " seconds ago"
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return str(second_diff / 60) + " minutes ago"
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return str(second_diff / 3600) + " hours ago"
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return str(day_diff) + " days ago"
    if day_diff < 31:
        return str(day_diff / 7) + " weeks ago"
    if day_diff < 365:
        return str(day_diff / 30) + " months ago"
    return str(day_diff / 365) + " years ago"

def get_reviews():
    start_idx = int(request.vars.start_idx) if request.vars.start_idx is not None else 0
    end_idx = int(request.vars.end_idx) if request.vars.end_idx is not None else 0
    # We just generate a lot of of data.
    reviews = []
    has_more = False
    already_reviewed = False
    rows = db(db.user_review.reviewed_id == request.vars.id).select(db.user_review.ALL, orderby=~db.user_review.created_on, limitby=(start_idx, end_idx + 1))
    current_user = auth.user.id if auth.user_id is not None else None
    for i, r in enumerate(rows):
        if i < end_idx - start_idx:
            # Check if I have a track or not.
            if r.user_id == current_user:
                already_reviewed = True
            t = dict(
                id = r.user_id,
                title = r.title,
                description = r.description,
                vote = r.vote,
                created_on_readable = pretty_date(r.created_on),
            )
            reviews.append(t)
        else:
            has_more = True
    logged_in = auth.user_id is not None
    return response.json(dict(
        reviews=reviews,
        logged_in=logged_in,
        has_more=has_more,
        current_user=auth.user.id if logged_in else None,
        already_reviewed=already_reviewed,
    ))

# Note that we need the URL to be signed, as this changes the db.
@auth.requires_signature(hash_vars=False)
def add_review():
    t_id = db.user_review.insert(
        reviewed_id = request.vars.id,
        title = request.vars.review_title,
        description = request.vars.review_description,
        vote = request.vars.vote,
        user_id = int(session.auth.user.id) if session.auth else None
    )
    t = db.user_review(t_id)
    return response.json(dict(review=t))

@auth.requires_signature()
def edit_review():
    p = db.user_review(request.vars.review_id)
    p.title = request.vars.edit_text
    p.update_record()
    return "ok"


@auth.requires_signature()
def del_review():
    db(db.user_review.id == request.vars.review_id).delete()
    return "ok"
