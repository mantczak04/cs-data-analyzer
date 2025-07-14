# frontend/pages/1_About.py

import streamlit as st

# Ustawia tytuł i ikonę w zakładce przeglądarki (opcjonalne, ale dobra praktyka)
st.set_page_config(
    page_title="About CS Analyzer",
    page_icon="ℹ️",
)

st.title("About CS Analyzer ℹ️")

st.markdown("""
### What is this application?

This is an AI-powered analysis tool for Counter-Strike match data. 
You can ask questions in natural language (any language you want) about recent S-tier professional matches, 
and the app will find the answers in the database and show you the results.

### What matches are in the database?
Recent* 553 maps played in S-tier: Blast Austin Major, IEM Dallas 2025, PGL Astana 2025, BLAST Rivals Spring 2025, IEM Melbourne 2025, PGL Bucharest 2025, BLAST Open Spring 2025, EPL Season 2.
            
**some matches weren't loaded to the database due to corrupted .dem files*

### What questions can I ask?

`show me teams that have highest eco/force-buy vs full rounds % winrate on de_nuke,  as T side, divide it on bombsites a/b`

`show me top 5 players with highest ADR on de_ancient (>100 rounds played on de_ancient)`
            
`show me all players that have most damage dealt by each hitgroup
name | hitgroup name | total damage dealt | total damage dealt to this hitgroup | % (hitgroup damage/total damage)`
            
`show teams with best % of won rounds in post-plant situations as CT on every map, bombsite A/B seperately. (current map pool)`
            
`show me players from GamerLegion and % of how many their AK-47 shots are in velocity > 20`
            
`show me top 5 teams that have most amount of utility thrown as terrorists after 1:20 (80 seconds) of the round, at de_inferno. Show mean amount of flashbangs, infernos and smokes per such round.`
            

### Possible errors
Please remember that this is a very early stage product and we just started testing it.

- The model is overloaded:
Just wait few seconds, then try again. It should work.
- Query was correct, but no data was found:
If you believe the query should return data, please copy prompt and send it to dev.mantczak@gmail.com or [my X (twitter)](https://x.com/mantczaq).
- Basically every other error/bad data: please copy prompt and error and send it to dev.mantczak@gmail.com or [my X (twitter)](https://x.com/mantczaq).
---

*Created by @mantczaq.*
            
*Contact: dev.mantczak@gmail.com*
""")

# Możesz dodać więcej tekstu, obrazków (st.image), etc.