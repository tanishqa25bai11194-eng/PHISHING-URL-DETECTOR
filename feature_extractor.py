import tldextract

def extract_features(url):

    features = []

    # URL length
    features.append(len(url))

    # HTTPS
    features.append(1 if "https" in url else 0)

    # @ symbol
    features.append(1 if "@" in url else 0)

    # dash
    features.append(1 if "-" in url else 0)

    # subdomain
    ext = tldextract.extract(url)
    subdomain = ext.subdomain

    if subdomain == "":
        features.append(0)
    else:
        features.append(len(subdomain.split(".")))

    # digits
    digits = sum(c.isdigit() for c in url)
    features.append(digits)

    # suspicious words
    suspicious = ['login','verify','bank','secure','update']

    features.append(1 if any(word in url.lower() for word in suspicious) else 0)

    return features