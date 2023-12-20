---
type: rule
title: "DevOps – Stage 1: Do you know what things to measure?"
uri: things-to-measure
authors:
  - title: Adam Cogan
    url: https://ssw.com.au/people/adam-cogan
  - title: Matt Wicks
    url: https://ssw.com.au/people/matt-wicks
related: []
redirects:
  - devops-stage-1-do-you-know-what-things-to-measure
  - devops-–-stage-1-do-you-know-what-things-to-measure
created: 2016-03-07T17:14:29.000Z
archivedreason: null
guid: b641999b-541f-45b5-8cf4-d2f585ce1f9b
---
Before you begin your journey into DevOps, you should assess yourself and see where your project is at and where you can improve.

<!--https://form.jotform.com/233467607749873-->
<script src="https://form.jotform.com/static/feedback2.js" type="text/javascript"></script>
<script type="text/javascript">
  var JFL_233467607749873 = new JotformFeedback({
    formId: "233467607749873",
    base: "https://form.jotform.com/",
    windowTitle: "DevOps - What things to measure (Stage 1)",
    backgroundColor: "#cc4141",
    fontColor: "#FFFFFF",
    type: "false",
    height: Math.floor(window.innerHeight * 0.9),
    width: 700,
    openOnLoad: false,
  });
</script>
<script type="text/javascript">
  var ifr = document.getElementById("lightbox-233467607749873");
  if (ifr) {
    var src = ifr.src;
    var iframeParams = [];
    if (window.location.href && window.location.href.indexOf("?") > -1) {
      iframeParams = iframeParams.concat(
        window.location.href
          .substr(window.location.href.indexOf("?") + 1)
          .split("&")
      );
    }
    if (src && src.indexOf("?") > -1) {
      iframeParams = iframeParams.concat(
        src.substr(src.indexOf("?") + 1).split("&")
      );
      src = src.substr(0, src.indexOf("?"));
    }
    iframeParams.push("isIframeEmbed=1");
    ifr.src = src + "?" + iframeParams.join("&");
  }
  window.handleIFrameMessage = function (e) {
    if (typeof e.data === "object") {
      return;
    }
    var args = e.data.split(":");
    if (args.length > 2) {
      iframe = document.getElementById("lightbox-" + args[args.length - 1]);
    } else {
      iframe = document.getElementById("lightbox");
    }
    if (!iframe) {
      return;
    }
    switch (args[0]) {
      case "scrollIntoView":
        iframe.scrollIntoView();
        break;
      case "setHeight":
        iframe.style.height = args[1] + "px";
        if (
          !isNaN(args[1]) &&
          parseInt(iframe.style.minHeight) > parseInt(args[1])
        ) {
          iframe.style.minHeight = args[1] + "px";
        }
        break;
      case "collapseErrorPage":
        if (iframe.clientHeight > window.innerHeight) {
          iframe.style.height = window.innerHeight + "px";
        }
        break;
      case "reloadPage":
        window.location.reload();
        break;
      case "loadScript":
        if (!window.isPermitted(e.origin, ["jotform.com", "jotform.pro"])) {
          break;
        }
        var src = args[1];
        if (args.length > 3) {
          src = args[1] + ":" + args[2];
        }
        var script = document.createElement("script");
        script.src = src;
        script.type = "text/javascript";
        document.body.appendChild(script);
        break;
      case "exitFullscreen":
        if (window.document.exitFullscreen) window.document.exitFullscreen();
        else if (window.document.mozCancelFullScreen)
          window.document.mozCancelFullScreen();
        else if (window.document.mozCancelFullscreen)
          window.document.mozCancelFullScreen();
        else if (window.document.webkitExitFullscreen)
          window.document.webkitExitFullscreen();
        else if (window.document.msExitFullscreen)
          window.document.msExitFullscreen();
        break;
    }
    var isJotForm = e.origin.indexOf("jotform") > -1 ? true : false;
    if (
      isJotForm &&
      "contentWindow" in iframe &&
      "postMessage" in iframe.contentWindow
    ) {
      var urls = {
        docurl: encodeURIComponent(document.URL),
        referrer: encodeURIComponent(document.referrer),
      };
      iframe.contentWindow.postMessage(
        JSON.stringify({ type: "urls", value: urls }),
        "*"
      );
    }
  };
  window.isPermitted = function (originUrl, whitelisted_domains) {
    var url = document.createElement("a");
    url.href = originUrl;
    var hostname = url.hostname;
    var result = false;
    if (typeof hostname !== "undefined") {
      whitelisted_domains.forEach(function (element) {
        if (
          hostname.slice(-1 * element.length - 1) === ".".concat(element) ||
          hostname === element
        ) {
          result = true;
        }
      });
      return result;
    }
  };
  if (window.addEventListener) {
    window.addEventListener("message", handleIFrameMessage, false);
  } else if (window.attachEvent) {
    window.attachEvent("onmessage", handleIFrameMessage);
  }
</script>
<a class="btn lightbox-233467607749873"
  style="
    margin-top: 16px;
    text-transform: uppercase;
    font-size: 14px;
    text-decoration: none;
    cursor: pointer;
    display: inline-block;
    padding: 10px;
    font-family: inherit;
    text-shadow: none;
    user-select: none;
    transition: all, 0.1s, ease-in;
    background-color: #cc4141;
    border: 1px solid #cc4141;
    color: #ffffff;
  ">
  Take this survey to find out your DevOps index
</a>
