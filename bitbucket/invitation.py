URLS = {
    # invitation
    'SEND_INVITATION': 'invitations/%(username)s/%(repo_slug)s/%(email_address)s/',
}


class Invitation(object):
    """ This class provide invitation related methods to Bitbucket objects."""

    def __init__(self, bitbucket):
        self.bitbucket= bitbucket
        self.bitbucket.URLS.update(URLS)

    def invite(self, repo_slug, email, permission, **kwargs):
        """ Invites a user to a repository."""
        url = self.bitbucket.url(
            'SEND_INVITATION',
            username=self.bitbucket.username,
            repo_slug=repo_slug,
            email_address=email)
        return self.bitbucket.dispatch('POST', url, auth=self.bitbucket.auth, permission=permission, **kwargs)
