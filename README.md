# Social_Network_pro4
Django needs two templates for sending password reset links:
1. registration/password_reset_form.html to display the form used to request a password
reset email.
2. registration/password_reset_done.html to show a confirmation that a password reset
email was sent.

Deep Dive
With connections, have to follow these assumptions:
* Your users will be able to either follow or not follow another user.
* If they follow someone, they’ll see that user’s content. If they don’t, they won’t.
* Your users can follow a person without being followed back. Relationships in your
* social network can be asymmetrical, meaning that a user can follow someone and see their content without the reverse being true.
* Your users need to be aware of who exists so that they know whom they can
follow.
* Users should also be aware of who follows them.
* In your app’s most basic form, users won’t have many extra features available to them. You won’t implement a way to block people, and there won’t be a way to
directly respond to content that someone else posted.
