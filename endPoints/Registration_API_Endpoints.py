base_url="https://qa-practical.qa.swimlane.io/api/user"

class Registration_API_Endpoints:
    "Class for registration endpoints"

    def registration_url(self, suffix=''):
        """Append API end point to base URL"""
        return self.base_url + '/login/' + suffix
