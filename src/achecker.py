
import urllib
import lxml.etree
import re

WSID = '1a2a79c40eff51d114e564a55be3f59bad81fd16'
API = 'http://achecker.ca/checkacc.php'
WA_GUIDE = 'WCAG2-AA'
OUT = 'rest'


class Achecker(object):
    xml = None

    def __init__(self):
        pass

    def get_resource(self, url):
        self.xml = None
        api_url = '%s?uri=%s&id=%s&output=%s&guide=%s' % \
            (API, url, WSID, OUT, WA_GUIDE)

        response = urllib.urlopen(api_url).read()

        self.xml = lxml.etree.fromstring(str.encode(response))

    def get_total_errors(self):
        summary = self.xml.find("summary")
        print "Number of errors: " + summary.findtext('NumOfErrors')
        return int(summary.findtext('NumOfErrors'))

    def get_total_likely(self):
        summary = self.xml.find("summary")
        print "Number of likely: " + summary.findtext('NumOfLikelyProblems')
        return int(summary.findtext('NumOfLikelyProblems'))

    def get_total_problems(self):
        summary = self.xml.find("summary")
        print "Number of potential: " + \
            summary.findtext('NumOfPotentialProblems')
        return int(summary.findtext('NumOfPotentialProblems'))

    def get_wa_type_ids(self):
        error_type_known = {}
        error_type_potential = {}
        error_type_likely = {}
        results = self.xml.find("results")
        for tag in results.iterchildren():
            e_type = tag.findtext('resultType')
            msg = tag.findtext('errorMsg')
            e_id = [s for s in re.split('=|&|\"', msg) if s.isdigit()]

            if e_type == 'Error':
                if e_id[0] in error_type_known:
                    error_type_known[e_id[0]] += 1
                else:
                    error_type_known[e_id[0]] = 1

            if e_type == 'Potential Problem':
                if e_id[0] in error_type_potential:
                    error_type_potential[e_id[0]] += 1
                else:
                    error_type_potential[e_id[0]] = 1

            if e_type == 'Likely Problem':
                if e_id[0] in error_type_likely:
                    error_type_likely[e_id[0]] += 1
                else:
                    error_type_likely[e_id[0]] = 1

        print error_type_known
        print error_type_potential
        print error_type_likely
        return error_type_known, error_type_potential, error_type_likely
