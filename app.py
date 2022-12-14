from pathlib import Path
import json
import random

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain


THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
CSS_FILE = THIS_DIR / "style" / "style.css"
LOTTIE_MUSIC = THIS_DIR / "assets" / "music_animation.json"
LOTTIE_CHRISTMAS = THIS_DIR / "assets" / "christmas_animation.json"

LINKS = {
    "Cadena Dial": r"https://20103.live.streamtheworld.com/CADENADIALAAC.aac?csegid=2000&gdpr=1&gdpr_consent=CPd2dsAPd2dsAAHABBENCcCsAP_AAAAAAAAAI8Nf_X__b3_j-_5___t0eY1f9_7__-0zjhfdl-8N3f_X_L8X_2M7vF36pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2cr7NKJ7PEmnMbeydYGH9_n1_z-ZKY7_____77__-_______f__-_f___p_3____f_V_997fn9_____9_P___9v__9__________3__AAAASGgAwABBHgVABgACCPBSADAAEEeB0AGAAII8BIAMAAQR4GQAYAAgjwSgAwABBHghABgACCPAiADAAEEeAAA.f_gAAAAAAAAA&dist=cadenadial-web-tod-permanente&tdsdk=js-2.9&swm=false&pname=TDSdk&pversion=2.9&banners=none&burst-time=15&sbmid=392354e8-aecc-4978-8aae-3577386efef4",
    "FreeCodeCamp": r"https://coderadio-relay-nyc.freecodecamp.org/radio/8010/radio.mp3",
    "Classical music": r"https://live.streams.klassikradio.de/klassikradio-deutschland?aggregator=Webseite&mode=preroll&aw_0_1st.skey=1670323419&cb=417236132&listenerid=6f6d11d633694ff5b778770f7c6d2e47&aw_0_req.userConsentV2=CPjkTwAPjkTwAAFADBDECtCoAP_AAAAAAAYgF7QDgACAAVABBACcAKIAWABaADIAJ4AbgBXADVAIQARMBeYC9gAAAEhIAMAAQL2DQAYAAgXsIgAwABAvYVABgACBewyADAAEC9h0AGAAIF7EIAMAAQL2JQAYAAgXsUgAwABAvYAA.YAAAAAAAAAAA",
    "Replay.FM": r"https://listener3.mp3.tb-group.fm/rp.mp3",
    "Heimatliebe": r"https://rhm1.de/listen.mp3",
    "Italian Radio": r"https://italianradio.streamingmedia.it/play",
    "Chilltrax": r"https://streamssl.chilltrax.com/stream/1/",
    "Radio Bollerwagen": r"https://ffn-de-hz-fal-stream09-cluster01.radiohost.de/radiobollerwagen_mp3-192",
    "Schlagerradio.FM": r"https://rautemusik-de-hz-fal-stream11.radiohost.de/schlager?ref=rmwp&listenerid=b2641d1a5f4d26f02360c0245295914c&awparams=companionAds:true",
    "Antenne Bayern Weihnachtshits": r"https://s8-webradio.antenne.de/weihnachts-hits/stream?aw_0_1st.playerId=AntenneBayernWebPlayer&aw_0_1st.listenerid=b2641d1a5f4d26f02360c0245295914c&aw_0_1st.skey=1670250928691&aw_0_req.userConsentV2=CPjhA0APjhA0AAFADBDECtCsAP_AAAAAAAYgINBZ5D5cTWFBeXx7QPs0eYwf11AVImAyChKBA6ABSDIAcLQEkmASMAyAAAACAAoEIBIBAAAkCAEEAEAQQIAAABHkAgAEhAEIICBEABERAAAACAIKCAAAAQAIAAARIgAAmQCAQ0LmRFQAgIAQJAAAhAgAAAAEAgMAAAAAAAIAAAAAgAAAAQAAAEhIAMAAQQaDQAYAAgg0IgAwABBBoVABgACCDQyADAAEEGh0AGAAIINEIAMAAQQaJQAYAAgg0UgAwABBBoAA.YAAAAAAAAAAA&companionAds=true&companion_zone_alias=41%2C42%2C40%2C731%2C752%2C756%2C768&aw_0_adx.1203antenne=431316722076978165",
    "Country Antenne": r"https://s1-webradio.rockantenne.de/country-antenne/stream?aw_0_1st.playerId=RockAntenneWebPlayer&aw_0_1st.listenerid=b2641d1a5f4d26f02360c0245295914c&aw_0_1st.skey=1670252848652&aw_0_req.userConsentV2=CPjhA0APjhA0AAFADBDECtCsAP_AAAAAAAYgINBZ5D5cTWFBeXx7QPs0eYwf11AVImAyChKBA6ABSLIAcLQEkmASMAyAAAACAAoEIBIBAAAkAAEEAEAQQIAAABHkAgAEhAEIICBEABERAAAACAIKCAAAAQAIAAARIgAAmQCAQ0LmRFQAgIAQJAAAhIgAAAAEAgMAAAAAAAIAAAAAgAAAAQMEgBAA4AYIASEgAwABBBoNABgACCDQiADAAEEGhkAGAAIINCoAMAAQQaHQAYAAgg0QgAwABBBolABgACCDRSADAAEEGgAA.YAAAAAAAAAAA&companionAds=true&companion_zone_alias=41%2C42%2C40%2C731%2C752%2C756%2C768&aw_0_adx.1215antenne=4313169152559100191",
    "Rock Antenne": r"https://s4-webradio.rockantenne.de/rockantenne/stream?aw_0_1st.playerId=RockAntenneWebPlayer&aw_0_1st.listenerid=b2641d1a5f4d26f02360c0245295914c&aw_0_1st.skey=1670252909642&aw_0_req.userConsentV2=CPjhA0APjhA0AAFADBDECtCsAP_AAAAAAAYgINBZ5D5cTWFBeXx7QPs0eYwf11AVImAyChKBA6ABSLIAcLQEkmASMAyAAAACAAoEIBIBAAAkAAEEAEAQQIAAABHkAgAEhAEIICBEABERAAAACAIKCAAAAQAIAAARIgAAmQCAQ0LmRFQAgIAQJAAAhIgAAAAEAgMAAAAAAAIAAAAAgAAAAQMEgBAA4AYIASEgAwABBBoNABgACCDQiADAAEEGhkAGAAIINCoAMAAQQaHQAYAAgg0QgAwABBBolABgACCDRSADAAEEGgAA.YAAAAAAAAAAA&companionAds=true&companion_zone_alias=41%2C42%2C40%2C731%2C752%2C756%2C768&aw_0_adx.1215antenne=4313169152559100191",
    "[Nightride] Original": r"https://stream.nightride.fm/nightride.mp3",
    "[Nightride] ChillSynth": r"https://stream.nightride.fm/chillsynth.mp3",
    "[sunshine-life] Original": r"https://sunsl.streamabc.net/sunsl-sunshinelive-mp3-192-3047475?sABC=63888666%231%233os27ssrq7506979p3po65o4o76n9r79%23ubzrcntr&context=fHA6LTE=&aw_0_1st.skey=1669891653&cb=187180982&aw_0_1st.playerid=sunshine-live_web&aw_0_req.userConsentV2=CPjADcAPjADcAAFADBDECsCsAP_AAEPAAAYgI9td_H__bW9j-f5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwX52E7NF36tq4KmR4ku1LBIQNlHMHUDUmwaokVryHsak2cpyNKJ7BEknMZOydYGF9Pmxtj-QKY7_5_d3bx2D-t_9v-39z338VXn3d53-_03PDdV599Dfn9fR_b89KP9958v4v8_____3_e__3_74I9gEmGrcQBdmWODNoGEUCIEYVhIVQKACCgGFogMAHBwU7KwCfWECABAKAIwIgQ4AowIBAAAJAEhEAEgRYIAAARAIAAQAIgEIAGBgEFgBYGAQAAgGgYohQACBIQZEBEUpgQFQJBAS2VCCUFUhphAFWWAFBIjYqABEEgIpAAEBYOAYIkBKxYIEmKN8gBGCFAKJUIAgaADAAEEexEAGAAII9ioAMAAQR7GQAYAAgj2AAA.YAAAAAAAAAAA&aw_0_1st.kuid=xz8ugfagr&aw_0_1st.ksg=[%22vz9c46692%22]&gfksui={%22id%22:%22E449F63BDF07B7D88F01690D527E5A52E23C16A073B9DEAFCC39EFB1%22,%22cd%22:1669191977,%22lt%22:1732263977,%22apps%22:{%22SuiGen%22:%222.5.5%22,%22VMS%22:%222.0.4%22}}&listenerid=3bf27ffed7506979c3cb65b4b76a9e79&amsparams=playerid:homepage;skey:1669891686",
    "[sunshine-life] Charts": r"https://sunsl.streamabc.net/sunsl-charts-mp3-192-1193432?sABC=6388856o%231%233os27ssrq7506979p3po65o4o76n9r79%23ubzrcntr&context=fHA6LTE=&aw_0_1st.skey=1669891403&cb=508370959&aw_0_1st.playerid=sunshine-live_web&aw_0_req.userConsentV2=CPjADcAPjADcAAFADBDECsCsAP_AAEPAAAYgI9td_H__bW9j-f5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwX52E7NF36tq4KmR4ku1LBIQNlHMHUDUmwaokVryHsak2cpyNKJ7BEknMZOydYGF9Pmxtj-QKY7_5_d3bx2D-t_9v-39z338VXn3d53-_03PDdV599Dfn9fR_b89KP9958v4v8_____3_e__3_74I9gEmGrcQBdmWODNoGEUCIEYVhIVQKACCgGFogMAHBwU7KwCfWECABAKAIwIgQ4AowIBAAAJAEhEAEgRYIAAARAIAAQAIgEIAGBgEFgBYGAQAAgGgYohQACBIQZEBEUpgQFQJBAS2VCCUFUhphAFWWAFBIjYqABEEgIpAAEBYOAYIkBKxYIEmKN8gBGCFAKJUIAgaADAAEEexEAGAAII9ioAMAAQR7GQAYAAgj2AAA.YAAAAAAAAAAA&aw_0_1st.kuid=xz8ugfagr&aw_0_1st.ksg=[%22vz9c46692%22]&listenerid=3bf27ffed7506979c3cb65b4b76a9e79&gfksui={%22id%22:%22E449F63BDF07B7D88F01690D527E5A52E23C16A073B9DEAFCC39EFB1%22,%22cd%22:1669191977,%22lt%22:1732263977,%22apps%22:{%22SuiGen%22:%222.5.5%22,%22VMS%22:%222.0.4%22}}&amsparams=playerid:homepage;skey:1669891435",
    "[sunshine-life] Eurodance": r"https://sunsl.streamabc.net/sunsl-eurodance-mp3-192-9832422?sABC=638886n9%231%233os27ssrq7506979p3po65o4o76n9r79%23ubzrcntr&context=fHA6LTE=&aw_0_1st.skey=1669891722&cb=722501796&aw_0_1st.playerid=sunshine-live_web&aw_0_req.userConsentV2=CPjADcAPjADcAAFADBDECsCsAP_AAEPAAAYgI9td_H__bW9j-f5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwX52E7NF36tq4KmR4ku1LBIQNlHMHUDUmwaokVryHsak2cpyNKJ7BEknMZOydYGF9Pmxtj-QKY7_5_d3bx2D-t_9v-39z338VXn3d53-_03PDdV599Dfn9fR_b89KP9958v4v8_____3_e__3_74I9gEmGrcQBdmWODNoGEUCIEYVhIVQKACCgGFogMAHBwU7KwCfWECABAKAIwIgQ4AowIBAAAJAEhEAEgRYIAAARAIAAQAIgEIAGBgEFgBYGAQAAgGgYohQACBIQZEBEUpgQFQJBAS2VCCUFUhphAFWWAFBIjYqABEEgIpAAEBYOAYIkBKxYIEmKN8gBGCFAKJUIAgaADAAEEexEAGAAII9ioAMAAQR7GQAYAAgj2AAA.YAAAAAAAAAAA&aw_0_1st.kuid=xz8ugfagr&aw_0_1st.ksg=[%22vz9c46692%22]&gfksui={%22id%22:%22E449F63BDF07B7D88F01690D527E5A52E23C16A073B9DEAFCC39EFB1%22,%22cd%22:1669191977,%22lt%22:1732263977,%22apps%22:{%22SuiGen%22:%222.5.5%22,%22VMS%22:%222.0.4%22}}&listenerid=3bf27ffed7506979c3cb65b4b76a9e79&amsparams=playerid:homepage;skey:1669891753",
    "[sunshine-life] Melodic Beats": r"https://sunsl.streamabc.net/sunsl-sunshinelivehappy-mp3-192-2662405?sABC=6399qpn1%231%23ppo4074r9934sp7op6835o02p11r09r7%23ubzrcntr&mode=preroll&aw_0_1st.skey=1671027873&cb=322773796&aw_0_1st.playerid=sunshine-live_web&aw_0_req.userConsentV2=CPjADcAPjADcAAFADBDECsCsAP_AAEPAAAYgI9td_H__bW9j-f5_aft0eY1P9_r37uQzDhfNk-8F3L_W_LwX52E7NF36tq4KmR4ku1LBIQNlHMHUDUmwaokVryHsak2cpyNKJ7BEknMZOydYGF9Pmxtj-QKY7_5_d3bx2D-t_9v-39z338VXn3d53-_03PDdV599Dfn9fR_b89KP9958v4v8_____3_e__3_74I9gEmGrcQBdmWODNoGEUCIEYVhIVQKACCgGFogMAHBwU7KwCfWECABAKAIwIgQ4AowIBAAAJAEhEAEgRYIAAARAIAAQAIgEIAGBgEFgBYGAQAAgGgYohQACBIQZEBEUpgQFQJBAS2VCCUFUhphAFWWAFBIjYqABEEgIpAAEBYOAYIkBKxYIEmKN8gBGCFAKJUIAgaADAAEEexEAGAAII9ioAMAAQR7GQAYAAgj2AAA.YAAAAAAAAAAA&aw_0_1st.kuid=xz8ugfagr&aw_0_1st.ksg=[%22vz9c46692%22]&listenerid=ccb4074e9934fc7bc6835b02c11e09e7&gfksui=%2216710276168255A429F2A9FD79959A3E81374848C51F67507C795292%22&amsparams=playerid:homepage;skey:1671027873",
}


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.set_page_config(page_title="Radio Livestreams", page_icon=":radio:", initial_sidebar_state="collapsed")
rain(
    emoji="❄",
    font_size=36,
    falling_speed=5,
    animation_length="infinite",
)

load_css_file(CSS_FILE)
left_col, right_col = st.columns(2)
with left_col:
    st.write("")
    st.write("")
    st.header(":radio: Radio Livestreams")
with right_col:
    lottie_music = load_lottiefile(LOTTIE_CHRISTMAS)
    st_lottie(lottie_music, key="lottie-music", height=150)

surprise_radio, surprise_link = random.choice(list(LINKS.items()))
left_col, right_col = st.columns(2)
left_col.subheader("Surprise me 🎁")
right_col.audio(surprise_link, format="audio/ogg")
with st.expander("What am I listening to?"):
    st.write(f"You are listing to {surprise_radio}")
st.write("---")

for name, url in LINKS.items():
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.subheader(name)
    right_col.audio(url, format="audio/ogg")
