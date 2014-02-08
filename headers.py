#!/usr/bin/env python
#

import webapp2
import re
from google.appengine.ext import db
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import xml.etree.ElementTree as ET
import logging

headers = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Organization  - schema.org</title>
    <meta name="description" content="Schema.org is a set of extensible schemas that enables webmasters to embed
    structured data on their web pages for use by search engines and other applications." />
    <link rel="stylesheet" type="text/css"
          href="http://schema.org/search_files/schemaorg.css" />

    <link href="http://schema.org/search_files/prettify.css" type="text/css"
          rel="stylesheet" />
    <script type="text/javascript" src="http://schema.org/js/prettify.js">
    </script>
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js"></script>

<script type="text/javascript">
      $(document).ready(function(){
        prettyPrint();
        setTimeout(function(){

  $(".atn:contains(itemscope), .atn:contains(itemtype), .atn:contains(itemprop), .atn:contains(itemid), .atn:contains(time), .atn:contains(datetime), .atn:contains(datetime), .tag:contains(time) ").addClass(\'new\');
  $('.new + .pun + .atv\').addClass(\'curl\');

        }, 500);
      });
</script>

<style>

  .pln    { color: #444;    } /* plain text                 */
  .tag    { color: #515484; } /* div, span, a, etc          */
  .atn,
  .atv    { color: #314B17; } /* href, datetime             */
  .new    { color: #660003; } /* itemscope, itemtype, etc,. */
  .curl   { color: #080;    } /* new url                    */

</style>

</head>
<body>
    <div id="container">
        <div id="intro">
            <div id="pageHeader">
              <div class="wrapper">
                <h1>schema.org</h1>

<div id="cse-search-form" style="width: 400px;"></div>

<script type="text/javascript" src="http://www.google.com/jsapi"></script>
<script type="text/javascript">
  google.load(\'search\', \'1\', {language : \'en\', style : google.loader.themes.ESPRESSO});
  google.setOnLoadCallback(function() {
    var customSearchControl = new google.search.CustomSearchControl(\'013516846811604855281:nj5laplixaa\');
    customSearchControl.setResultSetSize(google.search.Search.FILTERED_CSE_RESULTSET);
    var options = new google.search.DrawOptions();
    options.enableSearchboxOnly("http://schema.org/docs/search_results.html", null, false, \'#\');
    customSearchControl.draw(\'cse-search-form\', options);
  }, true);
</script>


              </div>
            </div>
        </div>
    </div>

            <div id="selectionbar">
               <div class="wrapper">
                <ul>
                    <li >
                      <a href="docs/documents.html">Documentation</a></li>
                    <li class="activelink">
                      <a href="docs/schemas.html">Schemas</a></li>
                    <li >
                      <a href=".">Home</a></li>
                </ul>
                </div>

            </div>
        <div style="padding: 14px; float: right;" id="languagebox"></div>

  <div id="mainContent">
'''

def OutputSchemaorgHeaders (webapp) :
    webapp.response.write(headers)
