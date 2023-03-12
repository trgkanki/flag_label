# -*- coding: utf-8 -*-
#
# addon_template v20.5.4i8
#
# Copyright: trgk (phu54321@naver.com)
# License: GNU AGPL, version 3 or later;
# See http://www.gnu.org/licenses/agpl.html

from aqt.reviewer import Reviewer
from anki.hooks import wrap
from .flagLabel import getFlagLabel

from .utils.configrw import getConfig, setConfig

import json

def initCSS(self, *args):
    redText = getFlagLabel(1)
    orangeText = getFlagLabel(2)
    greenText = getFlagLabel(3)
    blueText = getFlagLabel(4)
    pinkText = getFlagLabel(5)
    turquoiseText = getFlagLabel(6)
    purpleText = getFlagLabel(7)

    self.web.eval("""
(function () {
  // innerHTML of style element is read-only. remove & recreate css
  $('#flag-label').remove()
  $('head').append(`
  <style id="flag-label">
    #_flag::after {
      display: inline-block;
      padding-left: 0.5em;
      transform: translateY(-0.2em);
      font-size: .6em;
      -webkit-text-stroke-width: initial;
      color: #666;
    }
    .nightMode #_flag::after {
      color: white;
    }
    #_flag[style*="rgb(255, 102, 102)"]::after, #_flag[style*="--flag1-fg"]::after, #_flag[style*="--flag-1"]::after {
      content: %s;
    }
    #_flag[style*="rgb(255, 153, 0)"]::after, #_flag[style*="--flag2-fg"]::after, #_flag[style*="--flag-2"]::after {
      content: %s;
    }
    #_flag[style*="rgb(119, 255, 119)"]::after, #_flag[style*="--flag3-fg"]::after, #_flag[style*="--flag-3"]::after {
      content: %s;
    }
    #_flag[style*="rgb(119, 170, 255)"]::after, #_flag[style*="--flag4-fg"]::after, #_flag[style*="--flag-4"]::after {
      content: %s;
    }
    #_flag[style*="rgb(240, 151, 228)"]::after, #_flag[style*="--flag5-fg"]::after, #_flag[style*="--flag-5"]::after {
      content: %s;
    }
    #_flag[style*="rgb(92, 207, 202)"]::after, #_flag[style*="--flag6-fg"]::after, #_flag[style*="--flag-6"]::after {
      content: %s;
    }
    #_flag[style*="rgb(159, 99, 211)"]::after, #_flag[style*="--flag7-fg"]::after, #_flag[style*="--flag-7"]::after {
      content: %s;
    }
  </style>
  `)
})()

""" % (
        json.dumps(redText),
        json.dumps(orangeText),
        json.dumps(greenText),
        json.dumps(blueText),
        json.dumps(pinkText),
        json.dumps(turquoiseText),
        json.dumps(purpleText)
    ))


Reviewer.nextCard = wrap(Reviewer.nextCard, initCSS, "after")
