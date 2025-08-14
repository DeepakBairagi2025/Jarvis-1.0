import webbrowser
import difflib # For string similarity matching

def open_website_by_name(website_name):
    # Dictionary mapping website names to their URLs
    websites = {
    'google': 'https://www.google.com',
    'youtube': 'https://www.youtube.com',
    'facebook': 'https://www.facebook.com',
    'twitter': 'https://www.twitter.com',
    'instagram': 'https://www.instagram.com',
    'linkedin': 'https://www.linkedin.com',
    'github': 'https://www.github.com',
    'stackoverflow': 'https://stackoverflow.com',
    'reddit': 'https://www.reddit.com',
    'wikipedia': 'https://www.wikipedia.org',
    'quora': 'https://www.quora.com',
    'amazon': 'https://www.amazon.com',
    'flipkart': 'https://www.flipkart.com',
    'snapdeal': 'https://www.snapdeal.com',
    'myntra': 'https://www.myntra.com',
    'udemy': 'https://www.udemy.com',
    'coursera': 'https://www.coursera.org',
    'edx': 'https://www.edx.org',
    'khanacademy': 'https://www.khanacademy.org',
    'medium': 'https://medium.com',
    'netflix': 'https://www.netflix.com',
    'hotstar': 'https://www.hotstar.com',
    'primevideo': 'https://www.primevideo.com',
    'zomato': 'https://www.zomato.com',
    'swiggy': 'https://www.swiggy.com',
    'canva': 'https://www.canva.com',
    'notion': 'https://www.notion.so',
    'gmail': 'https://mail.google.com',
    'yahoo': 'https://www.yahoo.com',
    'duckduckgo': 'https://www.duckduckgo.com',
    'bing': 'https://www.bing.com',
    'zoho': 'https://www.zoho.com',
    'pixabay': 'https://www.pixabay.com',
    'pexels': 'https://www.pexels.com',
    'unsplash': 'https://www.unsplash.com',
    'wordpress': 'https://www.wordpress.com',
    'blogger': 'https://www.blogger.com',
    'tumblr': 'https://www.tumblr.com',
    'trello': 'https://www.trello.com',
    'dropbox': 'https://www.dropbox.com',
    'drive': 'https://drive.google.com',
    'skype': 'https://www.skype.com',
    'zoom': 'https://zoom.us',
    'meet': 'https://meet.google.com',
    'figma': 'https://www.figma.com',
    'codepen': 'https://codepen.io',
    'replit': 'https://replit.com',
    'w3schools': 'https://www.w3schools.com',
    'geeksforgeeks': 'https://www.geeksforgeeks.org',
    'tutorialspoint': 'https://www.tutorialspoint.com',
    'udacity': 'https://www.udacity.com',
    'futurelearn': 'https://www.futurelearn.com',
    'javatpoint': 'https://www.javatpoint.com',
    'crunchyroll': 'https://www.crunchyroll.com',
    'openai': 'https://www.openai.com',
    'codeacademy': 'https://www.codecademy.com',
    'freecodecamp': 'https://www.freecodecamp.org',
    'codeforces': 'https://codeforces.com',
    'atcoder': 'https://atcoder.jp',
    'leetcode': 'https://leetcode.com',
    'hackerank': 'https://www.hackerrank.com',
    'hackernews': 'https://news.ycombinator.com',
    'producthunt': 'https://www.producthunt.com',
    'techcrunch': 'https://techcrunch.com',
    'thenextweb': 'https://thenextweb.com',
    'wired': 'https://www.wired.com',
    'cnn': 'https://www.cnn.com',
    'bbc': 'https://www.bbc.com',
    'ndtv': 'https://www.ndtv.com',
    'indiatimes': 'https://www.indiatimes.com',
    'moneycontrol': 'https://www.moneycontrol.com',
    'groww': 'https://www.groww.in',
    'zerodha': 'https://www.zerodha.com',
    'coinmarketcap': 'https://coinmarketcap.com',
    'tradingview': 'https://www.tradingview.com',
    'spotify': 'https://www.spotify.com',
    'soundcloud': 'https://soundcloud.com',
    'gaana': 'https://gaana.com',
    'wynk': 'https://wynk.in',
    'jiosaavn': 'https://www.jiosaavn.com',
    'telegram': 'https://web.telegram.org',
    'whatsapp': 'https://web.whatsapp.com',
    'discord': 'https://discord.com',
    'tiktok': 'https://www.tiktok.com',
    'snapchat': 'https://www.snapchat.com',
    'glassdoor': 'https://www.glassdoor.com',
    'naukri': 'https://www.naukri.com',
    'indeed': 'https://www.indeed.com',
    'monster': 'https://www.monster.com',
    'internshala': 'https://internshala.com',
    'timesjobs': 'https://www.timesjobs.com',
    'freelancer': 'https://www.freelancer.com',
    'fiverr': 'https://www.fiverr.com',
    'upwork': 'https://www.upwork.com',
    'behance': 'https://www.behance.net',
    'dribbble': 'https://dribbble.com',
    'envato': 'https://www.envato.com',
    'themeforest': 'https://themeforest.net',
    'githubpages': 'https://pages.github.com',
    'netlify': 'https://www.netlify.com',
    'vercel': 'https://vercel.com',
    'cloudflare': 'https://www.cloudflare.com',
    'aws': 'https://aws.amazon.com',
    'azure': 'https://azure.microsoft.com',
    'gcp': 'https://cloud.google.com'
    }

    # Convert the input to lowercase for case-insensitive matching
    website_name_lower = website_name.lower()

    #Check if the exact name exists in the dictionary
    if website_name_lower in websites:
        url = websites[website_name_lower]
        webbrowser.open(url)
        print(f"Opening {website_name}...")
    else:
        # Find the closest matching website using string similarity
        matches = difflib.get_close_matches(website_name_lower, websites.keys(), n=1, cutoff=0.6)
        if matches:
            closest_match = matches[0]
            url = websites[closest_match]
            webbrowser.open(url)
            print(f"Opening the closest match: {closest_match} at {url}...")
        else:
            print(f"Sorry, I don't have information about the website '{website_name}'.")

""" if __name__ == "__main__":
    # Example usage
    user_input = input("Enter the name of the website you want to open: ")
    open_website_by_name(user_input) """