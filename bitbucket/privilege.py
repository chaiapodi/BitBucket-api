URLS = {
    # privilege
    'GET_REPOSITORY_PRIVILEGES': 'privileges/%(username)s/%(repo_slug)s/',
    'DELETE_ALL_PRIVILEGES_REPOSITORY': 'privileges/%(username)s/%(repo_slug)s/',
}


class Privilege(object):
    """ This class provide privilege related methods to Bitbucket objects."""

    def __init__(self, bitbucket):
        self.bitbucket= bitbucket
        self.bitbucket.URLS.update(URLS)

    def get_repository(self, repo_slug, **kwargs):
        """ get a list of individual user privileges granted on a repository."""
        url = self.bitbucket.url(
            'GET_REPOSITORY_PRIVILEGES',
            username=self.bitbucket.username,
            repo_slug=repo_slug)
        return self.bitbucket.dispatch('GET', url, auth=self.bitbucket.auth, **kwargs)

    def delete_all_from_repository(self, repo_slug, **kwargs):
        """ Deletes all privileges from a repository."""
        url = self.bitbucket.url(
            'DELETE_ALL_PRIVILEGES_REPOSITORY',
            username=self.bitbucket.username,
            repo_slug=repo_slug)
        return self.bitbucket.dispatch('DELETE', url, auth=self.bitbucket.auth, **kwargs)
