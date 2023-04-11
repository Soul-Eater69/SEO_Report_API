from deepawali_seo_report.utils.lib import gradeCalculator


def performanceOrganizer(seo_obj):
    seo_data = dict()

    response_data = seo_obj.get_response_times()
    if response_data["server_response_time"] <= 0.5 and response_data["content_load_time"] <= 5 and response_data["script_load_time"] <= 10:
        passed = True
    else:
        passed = False
    seo_data["pageSpeed_data"] = {
        "pass": 1 if passed else 0,
        "required": 1,
        "data": response_data,
        "display_title": "Page Speed Info",
        "priority": 1,
        "recommendation": "Optimize your page for Mobile PageSpeed Insights.",
        "description": "Page load speed is critical to ensuring good user experience and is becoming a more important ranking factor. Load speed can be impacted by a multitude of factors however and may need technical resources to investigate.",
        "text": "Your page load is fast." if passed else "Your page loads slowly.",
        "expand_data": "Download Page Size refers to the total amount of file content that needs to be downloaded by the browser to view a particular webpage. This includes HTML, CSS, Javascript and Images, though can include a number of other file formats. Generally media files like images and videos are significantly larger than text files and make up the bulk of Download File Size, but also represent the largest optimization opportunity. An important distinction here is 'Download' vs 'Raw' file size. Modern web protocols compress files during transfer, meaning files are usually smaller to download than their actual or 'raw' size. So any manual optimizations you perform would be on the 'raw' file. Download Page Size is one of the biggest contributors to Page Load Speed, which can directly affect rankings, user experience and conversions.\n\nIt is important to ensure your Download File Size is as small as possible by removing unnecessary files and minifying and optimizing others. 5MB is a good metric to strive for, though modern websites are gradually increasing in size."
    }

    compression_data = seo_obj.get_compression_data()

    seo_data["download_data"] = {
        "pass": 1 if compression_data["sizes"]["total_compressed_size"] <= 5 else 0,
        "required": 1,
        "display_title": "Download Page Size",
        "priority": 1,
        "recommendation": "Optimize your page for lower download page size.",
        "description": "",
        "text": "Your page's file size is reasonably low which is good for Page Load Speed and user experience." if compression_data["sizes"]["total_compressed_size"] <= 5 else "Your page's file size is high which is not good for Page Load Speed and user experience.",
        "expand_data": "Download Page Size refers to the total amount of file content that needs to be downloaded by the browser to view a particular webpage. This includes HTML, CSS, Javascript and Images, though can include a number of other file formats. Generally media files like images and videos are significantly larger than text files and make up the bulk of Download File Size, but also represent the largest optimization opportunity. An important distinction here is 'Download' vs 'Raw' file size. Modern web protocols compress files during transfer, meaning files are usually smaller to download than their actual or 'raw' size. So any manual optimizations you perform would be on the 'raw' file. Download Page Size is one of the biggest contributors to Page Load Speed, which can directly affect rankings, user experience and conversions.\n\nIt is important to ensure your Download File Size is as small as possible by removing unnecessary files and minifying and optimizing others. 5MB is a good metric to strive for, though modern websites are gradually increasing in size."
    }

    seo_data["website_data"] = {
        "pass": 1 if compression_data["sizes"]["total_rate"] <= 40 else 0,
        "required": 1,
        "data": compression_data["sizes"],
        "display_title": "Website Compression (Gzip, Deflate, Brotli)",
        "priority": 1,
        "recommendation": "Compress your page resources for faster load time.",
        "description": "",
        "text": "Your website appears to be using a reasonable level of compression." if compression_data["sizes"]["total_rate"] <= 40 else "Your website does not appear to be using a reasonable level of compression.",
        "expand_data": "Modern web servers allow website files to be compressed as part of their transfer, often dramatically reducing the Download File Size and Page Load Speed of a page. There are several different compression algorithms used such as GZIP, Deflate and Brotli. Enabling compression can often represent a simple and quick win to performance, and most new web servers will have this enabled by default.\n\nYou should ensure that compression is enabled and working effectively on your web server. Sometimes compression may only be partially enabled for particular file types, or using an older compression method, so it is important to understand whether your server is configured as efficiently as possible. This may require the help of a developer to investigate."
    }

    seo_data["resource_data"] = {
        "pass": 0,
        "required": 0,
        "data": compression_data["counts"],
        "display_title": "Number of Resources",
        "description": "This check displays the total number of files that need to be retrieved from web servers to load your page.",
        "text": "",
        "expand_data": "When browsers display a modern website, they have to retrieve a wide variety of files including HTML, CSS, Javascript, Images and other media. As a general rule, every file that needs to be retrieved is another network request that needs to be made by the browser to the server, which can each face some connection overhead and add to Page Load Time.\n\nIt is a good idea to remove unnecessary files or consolidate smaller files with similar content like styles and scripts where possible to optimize performance."
    }

    http2_data = seo_obj.check_http2()
    seo_data["http2_data"] = {
        "pass": 1 if http2_data else 0,
        "required": 1,
        "display_title": "HTTP2 Usage",
        "description": "",
        "priority": 0,
        "recommendation": "It is recommended to use HTTP/2+ protocol.",
        "text": "Your website is using the recommended HTTP/2+ protocol." if http2_data else "Your website is not using the recommended HTTP/2+ protocol.",
        "expand_data": "HTTP is a technology protocol used by web browser to communicate with websites and is a cornerstone of the world wide web. HTTP/2 (and above) are newer versions of the HTTP protocol that offer significant peformance improvements. Older websites may be set to using an older HTTP protocol despite their web servers having been upgraded to support newer versions.\n\nIt is worth reviewing whether your website is configured to use the latest available HTTP protocol as it can provide immediate Page Load Speed improvements."
    }

    optimized_images = seo_obj.check_optimized_images()
    seo_data["optimizedImages_data"] = {
        "pass": 1 if optimized_images else 0,
        "required": 1,
        "display_title": "Optimize Images",
        "priority": 1,
        "recommendation": "Optimize images on the page.",
        "description": "",
        "text": "All of the images on your page appear to be optimized." if optimized_images else "Some images on your page need to be optimized.",
        "expand_data": "Image and media files in general tend to be the largest component of file size on most modern webpages. File size can directly impact how quickly a page loads, and subsequently the quality of the experience for users. Images in general can have a large range in how much they can be optimized. For example, a high quality photograph downloaded from a camera could be 16MB, but using a reasonable level of size reduction and optimization could comfortably reduce it to 150KB without a noticeable amount of quality loss.\n\nReview the images used on your site, starting from the largest in file size to determine if there are optimization opportunities. You can use common image editing tools like Photoshop or even free online compression tools to optimize them."
    }

    minification_data = seo_obj.check_minified_files()
    seo_data["minification_data"] = {
        "pass": 1 if not minification_data else 0,
        "required": 1,
        "priority": 2,
        "recommendation": "Minify your CSS and JS Files.",
        "display_title": "Minification",
        "description": "Minification is a reasonably simple way to reduce page size, and subsequently load time.",
        "text": "All of the Javascript ot CSS files on your page appear to be optimized." if not minification_data else "Some of your JavaScript or CSS files do not appear to be minified.",
        "expand_data": "Minification is a procedure run on code text files that can reduce the text size by removing white space and substituting common values or names with shorter versions. Minification also offers the additional value of making code much harder to read and reverse engineer by third parties. It is best practice to minify any exposed JS and CSS Files before publishing them to a live site.\n\nMinification can be done automatically through some development tools and website build procedures, or through minification CMS Plugins, or manually through minification tools available online."
    }

    deprecatedHTML_data = seo_obj.check_depricated_html()
    seo_data["deprecatedHTML_data"] = {
        "pass": 1 if not deprecatedHTML_data else 0,
        "required": 1,
        "display_title": "Deprecated HTML",
        "recommendation": "Remove any deprecated elements or attributes on the page.",
        "priority": 2,
        "description": "",
        "text": "No deprecated HTML tags have been found within your page." if not deprecatedHTML_data else "Deprecated HTML tags have been found in your page.",
        "expand_data": "HTML, like most coding languages, has had improvements made over time that has removed older features, either due to them simply being problematic, or more often replaced with something better. If you continue to use these older features in your page, you may at the bare minimum not get the expected functionality in your page, or in the worst case, break some execution.\n\nIt is recommended to identify and remove any old or 'deprecated' tags from your code. This could be done manually if you have HTML or web design skills, or could be done by upgrading the template and library versions on your website."
    }

    inlineStyles_data = seo_obj.check_inline_styles()
    seo_data["inlineStyles_data"] = {
        "pass": 1 if not inlineStyles_data["hasStyles"] else 0,
        "required": 1,
        "data": inlineStyles_data["inline_styles"],
        "recommendation": "Remove any inline CSS on the page.",
        "priority": 2,
        "display_title": "Inline Styles",
        "description": "Inline styles are an older coding practice and discouraged in favor of using CSS style sheets, due to their ability to degrade page load performance and unnecessarily complicate HTML Code.",
        "text": "Your page appears to be using inline styles." if inlineStyles_data["hasStyles"] else "Your page does not appear to be using inline styles.",
        "expand_data": "HTML provides the ability to embed UI styling attributes within individual HTML elements. Despite this feature being available, it is modern best practice to completely separate UI styling into separate CSS files. This separates functions and centralises UI styling into one place making it easier for example to upgrade the UI styling of a site independently of the page content and structure. Inline styles also have some particular problems in that they can degrade the page load performance of a page and unnecessarily complicate HTML code.\n\nInline Styles should be manually removed from the HTML code of a page and merged into separate CSS files, but may need the help of a designer to carefully consider their purpose and function."
    }

    amp_data = seo_obj.get_amp_data()

    seo_data["amp_data"] = {
        "pass": 0,
        "required": 0,
        "data": amp_data,
        "display_title": "Google Accelerated Mobile Pages (AMP)",
        "priority": 2,
        "recommendation": "Its better to have AMP enabled in your site.",
        "description": "",
        "text": "This page appears to have AMP Enabled." if amp_data["amp_runtime"] else "This page does not appear to have AMP Enabled.",
        "expand_data": "AMP or Accelerated Mobile Pages, was an initiative originally created by Google to help mobile pages load faster through adherence to a specific set of requirements. Some research demonstrated that AMP enabled pages would receive a ranking benefit. AMP has often been criticized and begun to be deprecated by particular browsers and frameworks."
    }

    for i in seo_data:
        seo_data[i]["category"] = "Performance"

    grade, percentage, grade_title, grade_text = gradeCalculator(
        seo_data, "Performance")
    seo_data["percentage"] = percentage
    seo_data["grade"] = grade
    seo_data["grade_title"] = grade_title
    seo_data["grade_text"] = grade_text

    return seo_data
