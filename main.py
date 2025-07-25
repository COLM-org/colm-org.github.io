# pylint: disable=global-statement,redefined-outer-name
import argparse
import csv
import glob
import json
import os

import yaml
from flask import Flask, jsonify, redirect, render_template, send_from_directory
from flask_frozen import Freezer
from flaskext.markdown import Markdown

site_data = {}
by_uid = {}


def main(site_data_path):
    global site_data, extra_files
    extra_files = ["README.md", "cfp.md", "program-overview.md"]
    # Load all for your sitedata one time.
    for f in glob.glob(site_data_path + "/*"):
        extra_files.append(f)
        name, typ = f.split("/")[-1].split(".")
        if typ == "json":
            site_data[name] = json.load(open(f))
        elif typ in {"csv", "tsv"}:
            site_data[name] = list(csv.DictReader(open(f)))
        elif typ == "yml":
            site_data[name] = yaml.load(open(f).read(), Loader=yaml.SafeLoader)

    for typ in ["papers", "speakers", "workshops"]:
        by_uid[typ] = {}
        for p in site_data[typ]:
            by_uid[typ][p["UID"]] = p

    print("Data Successfully Loaded")
    return extra_files


# ------------- SERVER CODE -------------------->

app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)
markdown = Markdown(app)


# MAIN PAGES


def _data():
    data = {}
    data["config"] = site_data["config"]
    return data


@app.route("/")
def index():
    return redirect("/index.html")


@app.route("/favicon.svg")
def favicon():
    return send_from_directory(site_data_path, "favicon.svg")


# TOP LEVEL PAGES


@app.route("/index.html")
def home():
    data = _data()
    data["readme"] = open("README.md").read()
    # data["committee"] = site_data["committee"]["committee"]
    return render_template("index.html", **data)


@app.route("/help.html")
def about():
    data = _data()
    data["FAQ"] = site_data["faq"]["FAQ"]
    return render_template("help.html", **data)


# @app.route("/papers.html")
# def papers():
#     data = _data()
#     data["papers"] = site_data["papers"]
#     return render_template("papers.html", **data)


# @app.route("/paper_vis.html")
# def paper_vis():
#     data = _data()
#     return render_template("papers_vis.html", **data)


# @app.route("/calendar.html")
# def schedule():
#     data = _data()
#     data["day"] = {
#         "speakers": site_data["speakers"],
#         "highlighted": [
#             format_paper(by_uid["papers"][h["UID"]]) for h in site_data["highlighted"]
#         ],
#     }
#     return render_template("schedule.html", **data)


@app.route("/workshops.html")
def workshops():
    data = _data()
    data["workshops"] = [
        format_workshop(workshop) for workshop in site_data["workshops"]
    ]
    return render_template("workshops.html", **data)


def extract_list_field(v, key):
    value = v.get(key, "")
    if isinstance(value, list):
        return value
    else:
        return value.split("|")


def format_paper(v):
    list_keys = ["authors", "keywords", "sessions"]
    list_fields = {}
    for key in list_keys:
        list_fields[key] = extract_list_field(v, key)

    return {
        "UID": v["UID"],
        "title": v["title"],
        "forum": v["UID"],
        "authors": list_fields["authors"],
        "keywords": list_fields["keywords"],
        "abstract": v["abstract"],
        "TLDR": v["abstract"],
        "recs": [],
        "sessions": list_fields["sessions"],
        # links to external content per poster
        "pdf_url": v.get("pdf_url", ""),  # render poster from this PDF
        "code_link": "https://github.com/Mini-Conf/Mini-Conf",  # link to code
        "link": "https://arxiv.org/abs/2007.12238",  # link to paper
    }


def format_workshop(v):
    list_keys = ["authors"]
    list_fields = {}
    for key in list_keys:
        list_fields[key] = extract_list_field(v, key)

    return {
        "id": v["UID"],
        "title": v["title"],
        "url": v["url"],
        "cfp_url": v["cfp_url"],
        # "organizers": list_fields["authors"],
        # "abstract": v["abstract"],
    }


# ITEM PAGES


# @app.route("/poster_<poster>.html")
# def poster(poster):
#     uid = poster
#     v = by_uid["papers"][uid]
#     data = _data()
#     data["paper"] = format_paper(v)
#     return render_template("poster.html", **data)


# @app.route("/speaker_<speaker>.html")
# def speaker(speaker):
#     uid = speaker
#     v = by_uid["speakers"][uid]
#     data = _data()
#     data["speaker"] = v
#     return render_template("speaker.html", **data)


# @app.route("/workshop_<workshop>.html")
# def workshop(workshop):
#     uid = workshop
#     v = by_uid["workshops"][uid]
#     data = _data()
#     data["workshop"] = format_workshop(v)
#     return render_template("workshop.html", **data)


@app.route("/chat.html")
def chat():
    data = _data()
    return render_template("chat.html", **data)


@app.route("/cfp.html")
def cfp():
    data = _data()
    data["cfp"] = open("cfp.md").read()
    return render_template("cfp.html", **data)


@app.route("/cfw.html")
def cfw():
    data = _data()
    data["cfw"] = open("cfw.md").read()
    return render_template("cfw.html", **data)


@app.route("/board.html")
def board():
    data = _data()
    data["board"] = site_data["committee"]["board"]
    return render_template("board.html", **data)


@app.route("/program-overview.html")
def program_overview():
    data = _data()
    data["program_overview"] = open("program-overview.md").read()
    return render_template("program-overview.html", **data)


@app.route("/dates.html")
def dates():
    data = _data()
    data["dates"] = open("dates.md").read()
    return render_template("dates.html", **data)


@app.route("/CoE.html")
def coe():
    data = _data()
    data["CoE"] = open("CoE.md").read()
    return render_template("CoE.html", **data)


@app.route("/sponsors.html")
def sponsors():
    data = _data()
    data["sponsors"] = site_data["sponsors"]["sponsors"]
    return render_template("sponsors.html", **data)


@app.route("/ReviewGuide.html")
def reviewguide():
    data = _data()
    data["ReviewGuide"] = open("ReviewGuide.md").read()
    return render_template("ReviewGuide.html", **data)


@app.route("/coi-policy.html")
def coi_policy():
    data = _data()
    data["coiPolicy"] = open("coi-policy.md").read()
    return render_template("coi-policy.html", **data)


@app.route("/committees.html")
def committees():
    data = _data()
    data["committee"] = site_data["committee"]["committee"]
    data["AreaChairs"] = open("AreaChairs.md").read()
    return render_template("committees.html", **data)


@app.route("/AuthorGuide.html")
def authorguide():
    data = _data()
    data["AuthorGuide"] = open("AuthorGuide.md").read()
    return render_template("AuthorGuide.html", **data)


@app.route("/ac-guidelines.html")
def ac_guidelines():
    data = _data()
    data["acGuidelines"] = open("ac-guidelines.md").read()
    return render_template("ac-guidelines.html", **data)


@app.route("/AreaChairs.html")
def areachairs():
    data = _data()
    data["AreaChairs"] = open("AreaChairs.md").read()
    return render_template("AreaChairs.html", **data)


@app.route("/CoC.html")
def coc():
    data = _data()
    data["CoC"] = open("CoC.md").read()
    return render_template("CoC.html", **data)


@app.route("/Keynotes.html")
def keynotes():
    data = _data()
    data["Keynotes"] = site_data["speakers"]
    return render_template("Keynotes.html", **data)


@app.route("/SpecialSessions.html")
def special_sessions():
    data = _data()
    data["special_sessions"] = site_data["special-sessions"]
    return render_template("SpecialSessions.html", **data)


@app.route("/AcceptedPapers.html")
def accepted_papers():
    data = _data()
    data["AcceptedPapers"] = site_data["accepted_papers"]
    return render_template("AcceptedPapers.html", **data)


@app.route("/survey.html")
def survey():
    data = _data()
    return render_template("survey.html", **data)


@app.route("/faq.html")
def faq():
    data = _data()
    data["FAQ"] = site_data["faq"]["FAQ"]
    return render_template("faq.html", **data)


@app.route("/plenary.html")
def plenary():
    data = _data()
    data["plenary"] = site_data["plenary"]["plenary"]
    data["plenary_content"] = open("plenary.md").read()
    return render_template("plenary.html", **data)


@app.route("/hotels.html")
def hotels():
    data = _data()
    data["hotels"] = open("hotels.md").read()
    return render_template("hotels.html", **data)


# FRONT END SERVING


# @app.route("/papers.json")
# def paper_json():
#     json = []
#     for v in site_data["papers"]:
#         json.append(format_paper(v))
#     return jsonify(json)


@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)


@app.route("/serve_<path>.json")
def serve(path):
    return jsonify(site_data[path])


# --------------- DRIVER CODE -------------------------->
# Code to turn it all static


@freezer.register_generator
def generator():
    # for paper in site_data["papers"]:
    #     yield "poster", {"poster": str(paper["UID"])}
    # for speaker in site_data["speakers"]:
    #     yield "speaker", {"speaker": str(speaker["UID"])}
    # for workshop in site_data["workshops"]:
    #     yield "workshop", {"workshop": str(workshop["UID"])}

    for key in site_data:
        yield "serve", {"path": key}


def parse_arguments():
    parser = argparse.ArgumentParser(description="MiniConf Portal Command Line")

    parser.add_argument(
        "--build",
        action="store_true",
        default=False,
        help="Convert the site to static assets",
    )

    parser.add_argument(
        "-b",
        action="store_true",
        default=False,
        dest="build",
        help="Convert the site to static assets",
    )

    parser.add_argument("path", help="Pass the JSON data path and run the server")

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()

    site_data_path = args.path
    extra_files = main(site_data_path)

    if args.build:
        freezer.freeze()
    else:
        debug_val = False
        if os.getenv("FLASK_DEBUG") == "True":
            debug_val = True

        app.run(port=5000, debug=debug_val, extra_files=extra_files)
