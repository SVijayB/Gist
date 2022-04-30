from rouge import Rouge

# Test 1
# Reference link: https://inshorts.com/en/news/zuckerbergs-wealth-increases-by-$11-billion-in-his-biggest-oneday-gain-ever-1651223978818.
model_out = """Meta Platforms Inc. shares soared 17.6% on Thursday after it reported that its flagship social-media network, Facebook, added more users than projected in the first quarter . 
That added $11 billion to its 37-year-old chief executive officer’s fortune, the biggest one-day increase he's ever had, 
according to Bloomberg Billionaires Index"""
reference = """Meta platform's 37-year-old CEO Mark Zuckerberg added $11 billion to his fortune in the biggest
one-day gain he has ever had, Bloombeg reported. His personal wealth surged as Meta shares soared 17.6% on
Thursday,the biggest one-day increase he's ever had after it reported that Facebook added more users than expected in first quarter of 2022."""
rouge = Rouge()
print(rouge.get_scores(model_out, reference))


# Test 2
# Reference link: https://www.inshorts.com/en/news/no-covid-testing-vaccination-certificates-for-char-dham-yatra-ukhand-govt-1651307372254.
model_out = """he Uttarakhand government has instructed all the devotees to register on the state's portal before their arrival . 
It is not mandatory for passengers and devotees arriving from the state borders to undergo COVID-19 testing, and present a vaccination certificate . 
Char Dham Yatra begins on May 3 ."""
reference = """It is not mandatory for the Char Dham Yatra passengers and devotees arriving from the state borders to undergo COVID-19 testing or present a COVID-19 vaccination certificate, an official confirmed. 
It's, however, mandatory for all the devotees to register on the state's tourism portal before their arrival, the official added. The Char Dham Yatra commences on May 3."""
rouge = Rouge()
print(rouge.get_scores(model_out, reference))
