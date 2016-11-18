import tempfile

def index():
    pass

def get_reviews():
    start_idx = int(request.vars.start_idx) if request.vars.start_idx is not None else 0
    end_idx = int(request.vars.end_idx) if request.vars.end_idx is not None else 0
    # We just generate a lot of of data.
    reviews = []
    has_more = False
    sum = 0
    number_votes = 0
    already_reviewed = False
    rows = db(db.user_review.reviewed_id == request.vars.id).select(db.user_review.ALL, orderby=~db.user_review.created_on, limitby=(start_idx, end_idx + 1))
    current_user = auth.user.id if auth.user_id is not None else None
    if (str(current_user) == request.vars.id):
        already_reviewed = True
    for i, r in enumerate(rows):
        if i < end_idx - start_idx:
            # Check if I have a track or not.
            if r.user_id == current_user:
                already_reviewed = True
            sum = sum + r.vote
            number_votes += 1
            t = dict(
                id = r.user_id,
                title = r.title,
                description = r.description,
                vote = r.vote,
                created_on_readable = pretty_date(r.created_on),
                current_user_name=id_to_user_name(str(r.user_id)),
                reviewed_id=r.reviewed_id,
            )
            reviews.append(t)
            logger.info("LOL")
            logger.info(reviews)
        else:
            has_more = True
    if len(reviews) > 0:
        average = sum / len(reviews)
    else:
        average = 0
    logged_in = auth.user_id is not None
    return response.json(dict(
        reviews=reviews,
        logged_in=logged_in,
        has_more=has_more,
        current_user=auth.user.id if logged_in else None,
        average_vote = average,
        already_reviewed=already_reviewed,
        number_votes = number_votes,
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
    p.title = request.vars.edit_title
    p.description = request.vars.edit_text
    p.update_record()
    return "ok"


@auth.requires_signature()
def del_review():
    db((db.user_review.reviewed_id == request.vars.reviewed_id) & (db.user_review.user_id == request.vars.current_user)).delete()
    return "ok"
