from django.test import TestCase
from sites.models import Site


class TestHomeView(TestCase):

    def test_home_view_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_home_view_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

    def test_create_site_code(self):
        new_site_code = 'TYO1'
        response = self.client.post('/',{'new_site_code':new_site_code})
        site_code = Site.objects.get(site_code = new_site_code)
        self.assertEqual(site_code.site_code,new_site_code)

    def test_site_codes_arent_duplicated(self):
        site_code = 'TYO1'
        Site.objects.create(site_code=site_code)
        response = self.client.post('/',{'new_site_code':site_code})
        self.assertContains(response,'Site already exists')

    def test_site_code_is_valid(self):
        #format NRT5 (3 letters 1 Number)
        #only tes1 should be valid
        test_codes = ['a','aaaa','123a','test1','tes1','1111','1234','']
        site='TYO1'
        for site_code in test_codes:
            response = self.client.post('/',{'new_site_code':site_code,'site':site})
            if response.status_code==302:
                if site_code == '':
                    self.assertRedirects(response,f'/sites/{site.lower()}')
                else:
                    self.assertRedirects(response,f'/sites/{site_code.lower()}')
            else:
                self.assertEqual(response.context['is_valid'],False)