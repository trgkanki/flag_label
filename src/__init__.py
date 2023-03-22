# -*- coding: utf-8 -*-
#
# addon_template v20.5.4i8
#
# Copyright: trgk (phu54321@naver.com)
# License: GNU AGPL, version 3 or later;
# See http://www.gnu.org/licenses/agpl.html

from aqt.reviewer import Reviewer
from anki.hooks import wrap
from .flags import getFlagLabel, flagDefs

from .utils.configrw import getConfig, setConfig

import json

def initCSS(self, *args):
    flagsCSS = "\n".join(["""\
    #_flag[style*="{color}"]::after, #_flag[style*="--flag{index}-fg"]::after, #_flag[style*="--flag-{index}"]::after {{
      content: {text};
    }}
""".format(
        color=flagDef.defaultColor,
        index=index,
        text=json.dumps(getFlagLabel(index))
      ) for index, flagDef in flagDefs.items()
    ])

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

%s
  </style>
  `)
})()

""" % (flagsCSS,))


Reviewer.nextCard = wrap(Reviewer.nextCard, initCSS, "after")
