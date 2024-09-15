import asyncio
import httpx
import json
import re
import requests

def get_between(text, start, end):
    """Extracts substring between two delimiters."""
    pattern = re.escape(start) + r'(.*?)' + re.escape(end)
    match = re.search(pattern, text)
    return match.group(1) if match else ""

async def main():
    await buy_async("41622033432642")


def save_html_to_file(html_content):
    # Define the output file path
    output_file = "checkout_page.html"
    
    # Write the HTML content to the file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"Checkout page source saved to {output_file}")


async def buy_async(item_id):
    done12 = 2  # Ensure done12 is initialized
    print("Adding To Cart!")

    # Set the parameters
    parameters = {
        "id": item_id,
        "quantity": "1"
    }

    # Create a session with cookies
    session = httpx.AsyncClient()
    headers = {
        "Origin": "https://nrml.ca/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json"
    }

    # Convert parameters to JSON
    json_payload = json.dumps(parameters)

    # Post request to add to cart
    response = await session.post("https://nrml.ca/cart/add.js", headers=headers, content=json_payload)

    if response.is_success:
        print("Added to cart:", response.text)
    else:
        print(f"Error adding to cart: {response.status_code}")

    # Fetch the checkout URL
    checkout_response = await session.get("https://nrml.ca/checkout.json", headers={"User-Agent": headers["User-Agent"]})
    checkout_url = checkout_response.url

    # Get the checkout details
    checkout_details_response = await session.get(checkout_url, headers={"User-Agent": headers["User-Agent"]})

    source = checkout_details_response.text

    # Print cookies for debugging
    print("Cookies:", session.cookies)

    # Extract the authenticity token and Shopify token
    authenticity_token = get_between(source, "authenticity_token", "/>").strip().replace('value=', '').replace('"', '@')
    authenticity_token = get_between(authenticity_token, "@", "@")

    data1 = get_between(source, "Shopify.Checkout.token", "Shopify.Checkout.currency").strip()
    data106 = data1.strip(' "=')

    print("Submitting Info!")

    # Set the URL for shipping rates
    site11 = "https://nrml.ca/cart/shipping_rates.json?shipping_address[zip]=J4W3J2&shipping_address[country]=CANADA&shipping_address[province]=QC"
    
    # Make the request for shipping rates
    response1111 = await session.get(site11, headers=headers)
    source112 = response1111.text

    # Extract name and price
    name = get_between(source112, "name", "presentment").strip('",:')
    price = get_between(source112.replace('"', '@'), "@price@", ",").strip('@')

    # Shipping ID
    shipping = f"shopify-{name}-{price}"
    print("Shipping ID:", shipping)

    # Set up the form data for shipping address
    form_data = {
        "checkout[shipping_address][first_name]": "Shoe",
        "checkout[shipping_address][last_name]": "Bot",
        "authenticity_token": data106,
        "commit": "Continue",
        "_method": "patch",
        "previous_step": "contact_information",
        "checkout[email]": "shoebot0@gmail.com",
        "checkout[shipping_address][phone]": "450-443-0358",
        "checkout[shipping_address][address1]": "6400 Boulevard Taschereau",
        "checkout[shipping_address][country]": "CANADA",
        "checkout[shipping_address][province]": "QC",
        "g-recaptcha-response": "",
        "checkout[shipping_address][city]": "Brossard",
        "checkout[shipping_address][zip]": "J4W3J2",
        "checkout[client_details][javascript_enabled]": "1",
        "checkout[buyer_accepts_marketing]": "1"
    }

    # Make the POST request
    checkout_url = f"https://nrml.ca/checkouts/{data106}"
    result = await session.post(checkout_url, data=form_data, headers=headers)

    print(checkout_url)
    # Extract gateway information
    response_content = result.text
    gateway = get_between(response_content, "checkout_payment_gateway_", "\"")
    gateway = ''.join(filter(str.isdigit, gateway))

    print("Gateway:", gateway)

    checkout_url = "https://nrml.ca/checkout"

        # Use requests to fetch the HTML page
        # Create a requests session
    requests_session = requests.Session()

        # Populate the requests session with cookies from the httpx session
    for cookie in session.cookies.jar:
        requests_session.cookies.set(cookie.name, cookie.value)

        # Make a GET request to fetch the checkout page
    response = requests_session.get(checkout_url, allow_redirects=True)
    if response.status_code == 200:
            # Save the page source
      save_html_to_file(response.text)
    else:
      print(f"Error: {response.status_code}")

    # Check if shipping method needs to be submitted
    if gateway:
        # Set up the form data for shipping method
        form_data_shipping = {
            "authenticity_token": data106,
            "_method": "patch",
            "previous_step": "shipping_method",
            "step": "payment_method",
            "checkout[shipping_rate][id]": shipping,
        }

        print("Submitting Shipping!")
        result_shipping = await session.post(checkout_url, data=form_data_shipping, headers=headers)

        # Get total price and authenticity token
        response_shipping_content = await session.get(checkout_url).text
        total = get_between(response_shipping_content, "checkout_total_price", ">")
        total = ''.join(filter(str.isdigit, total))

        authentic = get_between(response_shipping_content, "authenticity_token", ">").replace('"', '@').split('@')[1]

        print("Total:", total)
        print("Authenticity Token:", authentic)

        answer = ""

        if done12 == 2:
            print("Generating Payment Token!")
            parameters = {
                "number": "3411 111111 11111",
                "name": "Shoe Bot",
                "month": "09",
                "year": "2023",
                "verification_value": "932",
                "payment_session_scope": "nrml.ca"
            }

            string_payload = json.dumps({"credit_card": parameters, "payment_session_scope": "nrml.ca"})
            http_content = string_payload.encode('utf-8')

            async with httpx.AsyncClient() as client:
                client.headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
                result = await client.post("https://elb.deposit.shopifycs.com/sessions", content=http_content)

                response_content = result.text
                response_content = response_content.replace('"', '@')
                response_content = response_content[response_content.index(':') + 1:]
                answer = get_between(response_content, "@", "@")
                print(answer)

                done12 = 3

        if done12 == 3:
            async with httpx.AsyncClient(cookies=session.cookies) as client:
                form_content = {
                    "authenticity_token": authenticity_token,
                    "_method": "patch",
                    "previous_step": "payment_method",
                    "step": "",
                    "checkout[buyer_accepts_marketing]": "1",
                    "s": answer,
                    "checkout[payment_gateway]": "75922051",
                    "checkout[credit_card][vault]": "false",
                    "checkout[different_billing_address]": "false",
                    "checkout[remember_me]": "false",
                    "checkout[vault_phone]": "+15646436423",
                    "checkout[total_price]": total,
                    "complete": "1",
                    "checkout[client_details][browser_width]": "979",
                    "checkout[client_details][browser_height]": "631",
                    "checkout[client_details][javascript_enabled]": "1",
                }

                client.headers["origin"] = "https://pay.shopify.com"
                client.headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"

                print("Submitting Payment!")

                result = await client.post(f"https://nrml.ca/13343831/checkouts/{data106}", data=form_content)
                response_content = result.text

                result2 = await client.get(f"https://nrml.ca/13343831/checkouts/{data106}/processing")
                response_content2 = result2.text

                print("Processing!")
                while "Processing" in response_content2:
                    await asyncio.sleep(2)
                    result3 = await client.get(f"https://nrml.ca/13343831/checkouts/{data106}/processing")
                    response_content2 = result3.text

                    if "Card was declined" in response_content2:
                        print("Card was declined")
                        break
                    elif "Error" in response_content2:
                        print("Error occurred")
                        break
                    elif not response_content2:
                        print("Error occurred: Empty response")
                        break
                    else:
                        print("Payment processed successfully")
                        break

if __name__ == "__main__":
    asyncio.run(main())