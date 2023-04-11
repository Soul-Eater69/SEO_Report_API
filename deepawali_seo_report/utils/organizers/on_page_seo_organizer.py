from deepawali_seo_report.utils.lib import gradeCalculator


def seoOrganizer(seo_obj):
    seo_data = dict()

    title_data = seo_obj.get_title_data()
    seo_data["title_data"] = {
        "pass": 1 if title_data["title_length"] in range(10, 70) else 0,
        "required": 1,
        "display_title": "Title Tag",
        "priority": 0,
        "recommendation": "Include a title of length in the range of 10 - 70 characters.",
        "description": "You have a title tag of optimal length (between 10 and 70 characters)." if title_data["title_length"] in range(10, 70) else f"Your title length is {title_data['title_length']}, the optimal range is 10 and 70",
        "text": title_data["title_text"] if title_data["title_text"] else "Your page appears to be missing a title tag.",
        "length": title_data["title_length"],
        "priority": 2,
        "expand_data": "The Title Tag is an important HTML element that tells users and Search Engines what the topic of the webpage is and the type of keywords the page should rank for. The Title will appear in the Header Bar of a user's browser. It is also one of the most important (and easiest to improve) On-Page SEO factors.\nWe recommend setting a keyword rich Title between 10–70 characters. This is often simple to enter into your CMS system or may need to be manually set in the header section of the HTML code."
    }

    meta_data = seo_obj.get_metaTag_data()
    seo_data["meta_data"] = {
        "pass": 1 if meta_data else 0,
        "required": 1,
        "display_title": "Meta Tag Description",
        "priority": 0,
        "recommendation": "Add a Meta Tag Description.",
        "description": "You have a meta tag, which makes it easy for search engines to understand your content." if meta_data else "A meta description is important for search engines to understand the content of your page, and is often shown as the description text blurb in search results.",
        "text": meta_data if meta_data else "Your page appears to be missing a meta description tag.",
        "expand_data": "Meta Description is another important HTML element that explains more descriptively to Search Engines what your page is about. Meta Descriptions are often used as the text snippets used in Search Engine results (though Search Engines are inceasingly generating these themselves) and can help further signal to Search Engines what keywords your page should rank for.\nMake sure your page has a Meta Description included, and is at an optimum length (between 70 and 160 characters). Make your Meta Description text interesting and easy to comprehend. Use phrases and keywords relevant to the page and user that you would like to rank for. Meta Description is normally available to be updated in your CMS."
    }

    seo_data["serp_data"] = {
        "pass": 1,
        "required": 0,
        "display_title": "SERP Snippet Preview",
        "description": "This illustrates how your page may appear in Search Results. Note, this is intended as a guide and Search Engines are more frequently generating this content dynamically.",
        "expand_data": "The SERP Snippet illustrates how your page may be shown in Search Results for a particular query. Typically the page's Title, URL and Meta Description have been the main components utilized here, and hence could be carefully dictated, though Search Engines are more frequently building these snippets themselves to better represent the page content to their searchers.\nIt's important that the SERP Snippet is enticing for your searchers to click on, and accurately represents your content to avoid bounces or heavy re-writing by the Search Engine. You should keep these factors in mind when populating the page Title, Meta Description and URL."
    }

    hreflang_data = seo_obj.check_for_hrefLang()
    seo_data["hreflang_data"] = {
        "pass": 1 if hreflang_data else 0,
        "recommendation": "Include a Href Lang Tag.",
        "priority": 2,
        "required": 0,
        "display_title": "Hreflang Usage",
        "description": "Your page is making use of Hreflang attributes." if hreflang_data else "Your page is not making use of Hreflang attributes.",
        "expand_data": "Hreflang is an HTML attribute used to specify the language and geographical targeting of a page. It is commonly used together with the 'alternate' attribute in the code of a page to signal to Search Engines a list of alternative language or geographic versions of the current page.\nIf you have multiple versions of the same page in different languages, it is important to add Hreflang tags to tell Search Engines about these variations. This code may need to be manually added into the HTML code of your page, but is also often controlled by your CMS or plugin system if multi-lingual features are enabled."
    }

    language_data = seo_obj.get_lang()
    seo_data["language_data"] = {
        "pass": 1 if language_data else 0,
        "required": 1,
        "display_title": "Language",
        "priority": 2,
        "recommendation": "Specify the Language Used in the page.",
        "text": language_data if language_data else "",
        "description": "Your page is using the lang attribute." if language_data else "Your page is not using the lang attribute.",
        "expand_data": "The lang attribute is used to describe the intended language of the current page to user's browsers and Search Engines. Search Engines may use the lang attribute to return language specific search results to a searcher, and in the browser, lang attribute can signal the need to switch to a different language if it is different to the user's own preferred language.\nWe recommend adding the lang attribute to the HTML tag of every page to avoid any chance of misinterpretation of language. This may need to be manually added to the site's HTML code, or may be controlled by your CMS."
    }

    h1_data = seo_obj.get_H1_tag()
    seo_data["h1_data"] = {
        "pass": 1 if h1_data else 0,
        "required": 1,
        "priority": 0,
        "recommendation": "Its better to add H1 tags to highlight your headings.",
        "display_title": "H1 Header Tag Usage",
        "text": h1_data if h1_data else [],
        "description": "Your page has H1 Tag." if h1_data else "Your page does not have a H1 Tag.",
        "expand_data": "The H1 Header Tag is one of the most important ways of signaling to Search Engines the topic of a page and subsequently the keywords it should rank for. The H1 Tag normally appears as visible text in the largest font size on the page.\nWe recommend adding a H1 Header Tag near the top of your page content and include important keywords you would like to rank for. You should have one, and only one H1 tag on each page. If you are using a CMS, this would normally be entered into the core content section of the page."
    }

    headers_data = seo_obj.get_headings_data()
    seo_data["headers_data"] = {
        "pass": 1 if headers_data["total_h_tags"] > 0 else 0,
        "required": 1,
        "total_h_tags": headers_data["total_h_tags"],
        "display_title": "H2-H6 Header Tag Usage",
        "priority": 1,
        "recommendation": "Use Header tags to represent the headings.",
        "tags": headers_data["tags"],
        "text": headers_data["headings_data"] if headers_data["total_h_tags"] > 0 else [],
        "description": "Your page is making use of multiple levels of Header Tags." if headers_data["total_h_tags"] > 0 else "Your page is not making use of multiple levels of Header Tags.",
        "expand_data": "The H2-H6 Header Tags are an important way of organizing the content of your page and signaling to Search Engines the longer tail topics your page should rank for.\nWe recommend including at least 2 other Header Tag levels on your page (such as H2 and H3) in addition to the H1. It is useful to also include important keywords in these Header Tags. These would be added to the core content section of your page."
    }

    content_data = seo_obj.get_text_count()
    seo_data["content_data"] = {
        "pass": 1 if content_data > 0 else 0,
        "required": 1,
        "display_title": "Amount of Content",
        "text": content_data if content_data > 0 else 0,
        "priority": 1,
        "recommendation": "Please use good level of textual content.",
        "description": "Your page has a good level of textual content, which will assist in it's ranking potential." if content_data > 250 else "Your page does not have a good level of textual content, which will affect it's ranking potential.",
        "expand_data": "Numerous studies have shown that there is a relationship between the amount of content on a page (typically measured in word count) and it's ranking potential - generally longer content will rank higher. Obviously content also needs to be topically relevant, keyword rich and highly readable for the visitor. Note, in our assessment, we look at all selectable text on the page at load time, not hidden content.\nAs a general guideline, it is recommended to have atleast 500 words of content on a page to give it some ranking potential. However this should be considered on a case by case basis. It may not be relevant for particular pages like 'contact us' pages for example."
    }

    images_data = seo_obj.get_image_attr_data()
    seo_data["images_data"] = {
        "pass": 1 if images_data["total_imgs"] == 0 else 0,
        "required": 1,
        "display_title": "Image Alt Attributes",
        "total_imgs": images_data["total_imgs"],
        "priority": 0,
        "recommendation": "Add Alt attributes to all images.",
        "missing_attrs": images_data["tags_without_alt_len"],
        "text": images_data["total_imgs"] if images_data["total_imgs"] > 0 else [],
        "tags": images_data["tags"],
        "description": "You have images on your page that are missing Alt attributes." if images_data["total_imgs"] > 0 else "You dont have images on your page that are missing Alt attributes.",
        "expand_data": "Alternate Image Text or Alt Text is descriptive text that is displayed in place of an image if it can't be loaded, as well as a label on an image when it is moused over in the browser, to give more information to the visitor. Additionally, Search Engines use provided Alt Text to better understand the content of an image. Image SEO is not widely known, but having your image rank for image searches is an overlooked way of gaining traffic and backlinks to your site.\nWe recommend adding useful and keyword rich Alt Text for pages's main images, in particular those that could have ranking potential. This should be considered on a case-by-case basis. Often there may be imagery such as UI components or tracking pixels where it may not be useful to add Alt Text, though we have tried to filter a number of these out in our analysis."
    }

    canonical_data = seo_obj.get_canonical_tag()
    seo_data["canonical_data"] = {
        "pass": 1 if canonical_data else 0,
        "required": 1,
        "display_title": "Canonical Tag",
        "priority": 2,
        "recommendation": "Use the canonical tag to specify the preferred version of a page.",
        "text": "",
        "description": "Your page is using the Canonical Tag." if canonical_data else "Your page is not using the Canonical Tag.",
        "expand_data": "The Canonical Tag is a HTML Tag that tells Search Engines the primary URL of a page. URLs can have multiple versions due to things like parameters being passed or www and non-www versions, resulting in potential duplicate content. Google recommends all pages specify a Canonical for this reason.\nYou may need to determine what the primary preferred version of the page is. Often the CMS may manage this, or provide the ability to specify it."
    }

    no_index_tag_data = seo_obj.get_noindex_data()

    seo_data["no_index_tag_data"] = {
        "pass": 1 if not no_index_tag_data["noindex_tag"] else 0,
        "required": 1,
        "display_title": "Noindex Tag Test",
        "priority": 1,
        "recommendation": "Check for any noindex tags on the page.",
        "text": "",
        "description": "Your page is not using the Noindex Tag which prevents indexing." if not no_index_tag_data["noindex_tag"] else "Your page is using the Noindex Tag which prevents indexing.",
        "expand_data": "A critical part of a page's ranking potential is ensuring that it can actually be accessed by Search Engines. The Noindex Tag, when used on pages, tells Search Engines to ignore a page, and can destroy out it's ranking ability. Sometimes these tags are added intentionally for low value pages, but sometimes they are left over unintentionally from a theme or template that has been used on the site, or forgotten to be removed by a developer when a website moves from design and testing to live usage.\nIf you want the page to rank and it's using a Noindex Tag, you will need to remove the tag from your page's HTML entirely. This may require access to the frontend HTML code, and may need to be done by a developer. If you are using a CMS, you may have an option enabled to prevent indexing of the page, which should be turned off."
    }

    seo_data["no_index_header_data"] = {
        "pass": 1 if not no_index_tag_data["noindex_header"] else 0,
        "required": 1,
        "display_title": "Noindex Header Test",
        "text": "",
        "priority": 1,
        "recommendation": "Remove any noindex headers from your website.",
        "description": "Your page is not using the Noindex Header Tag which prevents indexing." if not no_index_tag_data["noindex_header"] else "Your page is using the Noindex Header Tag which prevents indexing.",
        "expand_data": "A critical part of a page's ranking potential is ensuring that it can actually be accessed by Search Engines. The Noindex Header is another Noindexing method that tells Search Engines to ignore a page, and can destroy out it's ranking ability. Sometimes these tags are added intentionally for low value pages, but sometimes they are left over unintentionally from a theme or template that has been used on the site, or forgotten to be removed by a developer when a website moves from design and testing to live usage.\nIf you want the page to rank and it's using a Noindex Header, you will need to remove the Noindex Header from your page. This may require access to the backend code, and may need to be done by a developer. If you are using a CMS, you may have an option enabled to prevent indexing of the page, which should be turned off."
    }

    ssl_data = seo_obj.get_ssl_data()
    seo_data["ssl_data"] = {
        "pass": 1 if ssl_data["ssl"] else 0,
        "required": 1,
        "display_title": "SSL Enabled",
        "priority": 1,
        "recommendation": "Use SSL encryption on your website.",
        "text": "",
        "description": "Your website has SSL enabled." if ssl_data["ssl"] > 0 else "Your website has no SSL enabled.",
        "expand_data": "The robots.txt file includes important instructions to Search Engines on how to crawl a site, including instructions to ignore particular pages (effectively 'blocking' them). Sometimes these instructions are added intentionally for low value pages, but sometimes they are left over by mistake when a website goes live, or can be written incorrectly excluding more pages than desired.\nIf you want the page to rank and it's blocked by a rule in robots.txt, you may need to review your robots rules to understand why it's being blocked, and remove the rule. Because robots.txt instructions are a type of code, this may require the help of a developer to correct."
    }

    robots_data = seo_obj.get_robots_txt_data()
    seo_data["robots_data"] = {
        "pass": 1 if robots_data["robots"] else 0,
        "required": 1,
        "display_title": "Robots.txt",
        "text": "",
        "priority": 1,
        "recommendation": "Create a robots.txt file.",
        "description": "Your website appears to have a robots.txt file." if robots_data["robots"] else "Your website appears not to have a robots.txt file.",
        "expand_data": "Robots.txt is a text file that provides instructions to Search Engine crawlers on how to crawl your site, including types of pages to access or not access. It is often the gatekeeper of your site, and normally the first thing a Search Engine bot will access.We recommend always having a robots file in place for your site. These can be automatically created using a free online utility, Wordpress plugin, or your CMS's robots.txt creation process."
    }

    description = ""
    if robots_data["blocked"] == True:
        description = "Your page does appear to be blocked by robots.txt."

    elif robots_data["blocked"] == False:
        description = "Your page does not appear to be blocked by robots.txt."

    else:
        description = "Your page does not appear to have this data."

    seo_data["blocked_data"] = {
        "pass": 1 if robots_data["blocked"] else 0,
        "required": 1,
        "display_title": "Blocked by Robots.txt",
        "text": "",
        "priority": 1,
        "recommendation": "Review your robots.txt file to ensure its is not blocking any important pages.",
        "description": description,
        "expand_data": "The robots.txt file includes important instructions to Search Engines on how to crawl a site, including instructions to ignore particular pages (effectively 'blocking' them). Sometimes these instructions are added intentionally for low value pages, but sometimes they are left over by mistake when a website goes live, or can be written incorrectly excluding more pages than desired.\nIf you want the page to rank and it's blocked by a rule in robots.txt, you may need to review your robots rules to understand why it's being blocked, and remove the rule. Because robots.txt instructions are a type of code, this may require the help of a developer to correct."
    }

    xml_data = seo_obj.get_site_map()
    seo_data["xml_data"] = {
        "pass": 1 if xml_data else 0,
        "required": 1,
        "priority": 0,
        "recommendation": "Create a sitemap for your website.",
        "display_title": "XML Sitemaps",
        "text": "",
        "description": "Your website appears to have an XML sitemap." if xml_data else "Your website appears not to have an XML sitemap.",
        "expand_data": "A Sitemap is an XML data file on your site that lists all of your site's pages that are available for crawling together with other useful information like last update times and crawling priority. Sitemap files help Search Engines find all your pages to give them the highest chance of being indexed and ranked.\nWe recommend always having a Sitemaps file in place for your site. Sitemaps can be created manually using a utility, Wordpress plugin, or your CMS's Sitemap creation process. Additionally, the Sitemap should be referenced in your robots.txt file."
    }

    structured_data = seo_obj.get_structured_data()
    seo_data["structured_data"] = {
        "pass": 1 if structured_data["schema_type"] else 0,
        "required": 1,
        "priority": 0,
        "recommendation": "Use Schema.org markup.",
        "display_title": "Schema.org Structured Data",
        "text": "",
        "description": "You are using "+structured_data["schema_type"]+" Schema on your page." if structured_data["schema_type"] else "You are not using any Schema on your page.",
        "expand_data": "Schema.org Structured Data Markup is a collection of data tags that can be added to your site to allow Search Engines to more easily interpret the content and use it to enhance Search Results. For example there are tags for providing information about your Local Business such as address and phone number, or adding product information on e-commerce pages so that these products can be displayed in shopping aggregators like Google Shopping.\nIt is a good idea to start incorporating some relevant Schema.org tags into your site to improve interpretation and display by Search Engines."
    }

    for i in seo_data:
        seo_data[i]["category"] = "On-Page SEO"

    grade, percentage, grade_title, grade_text = gradeCalculator(
        seo_data, "On-Page SEO")
    seo_data["percentage"] = percentage
    seo_data["grade"] = grade
    seo_data["grade_title"] = grade_title
    seo_data["grade_text"] = grade_text

    return seo_data
