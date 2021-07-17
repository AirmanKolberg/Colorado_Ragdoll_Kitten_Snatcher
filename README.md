# The Colorado Ragdoll Kitten Snater Bot

My fiancée and I have been wanting to get a couple of ragdoll kittens for the little one for quite some
time now.  A breeder with whom we've been in touch has notified us that in the next week, their website
would be updated so that people can place deposits on the very limited litter.  At my fiancée's request,
I've created a quick and simple bot that requests the webpage where you'd normally place a deposit through
a PayPal order or something, and it looks for the specific tag notifying that the kittens will be ready
for deposits soon every minute.  If it is there, no big deal, it waits a minute and tries again.  However,
if it is gone (and therefore something has changed on that webpage), it should have caught the change 59
seconds after it was posted at worst, and it sends a text message and/or calls you and/or anybody else
to notify.  The text message also includes a link, so that I can simply click on it, then put a deposit
down to adopt two cats.

If you'd like, feel free to take this code and use it to kitten-snipe yourself, if you are looking for
a specific breed (such as ragdolls) where it is relatively difficult to find a decent and ethical
breeder.

## Steps

1. Ensure the dependencies are installed.  Whether it be `pip` or `pip3`, make sure to first run:
`pip install -r requirements.txt`
2. Change the name of `secrets_example.py` to `secrets.py`, and amend the variables within as per
the comment instructions found within that file.
3. You're done!  Run the app with `python3 app.py` and await to become the gaurdian of a/some new 
family member(s)!

*Note:  I do not advise going further to automate the payment/deposit process.  Seems odd for a cat, no?*

---

### Donations!
Consider donating, though of course not necessary!  🙂


| Donation Asset    | Donation Address|  
| :---------------- | :-------------: |
|  Cardano (ADA) | addr1q9jxsfd87g4f9rcl7x43lwxnkmklek279yw0fhwrsm3pjjal23me7f9yesnhs2fhpf05xd0deta3csgn4z433rze7yjsav8ejn|
| BitCoin (BTC)   | 33XbUGgEGx3oQ8wZEsdWBtZ6jncTPWoNtq| 
|  Ethereum (ETH) | 0x68D8928631f697820cf2bd9B275e5b39D6Cba020|
| Dogecoin (DOGE)   | DNJoCDAwwVcpRMH3wCeeCwRMpzUHW6uvbH|
|  Ripple (XRP) | rahunjARy7sb2AEc75xdzqSRuMeUPqXxF2|
| VeChain (VET)   | 0xeD36284Fb479F15620f5c8Af0996A723c6b5dc43|