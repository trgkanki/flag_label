# -*- coding: utf-8 -*-
#
# addon_template v20.5.4i8
#
# Copyright: trgk (phu54321@naver.com)
# License: GNU AGPL, version 3 or later;
# See http://www.gnu.org/licenses/agpl.html

from aqt.reviewer import Reviewer
from anki.hooks import wrap

from .utils.configrw import getConfig, setConfig

import json

def initCSS(self, *args):
    redText = getConfig('redText', '')
    orangeText = getConfig('orangeText', '')
    greenText = getConfig('greenText', '')
    blueText = getConfig('blueText', '')

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
    #_flag[style*="rgb(255, 102, 102)"]::after, #_flag[style*="--flag1-fg"]::after {
      content: %s;
    }
    #_flag[style*="rgb(255, 153, 0)"]::after, #_flag[style*="--flag2-fg"]::after {
      content: %s;
    }
    #_flag[style*="rgb(119, 255, 119)"]::after, #_flag[style*="--flag3-fg"]::after {
      content: %s;
    }
    #_flag[style*="rgb(119, 170, 255)"]::after, #_flag[style*="--flag4-fg"]::after {
      content: %s;
    }
  </style>
  `)
})()

""" % (
    json.dumps(redText),
    json.dumps(orangeText),
    json.dumps(greenText),
    json.dumps(blueText)
))

Reviewer.nextCard = wrap(Reviewer.nextCard, initCSS, "after")


