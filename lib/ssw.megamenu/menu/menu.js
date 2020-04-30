import React from 'react';
import styles from './menu.module.css';
import DesktopMenu from '../desktop-menu/desktop-menu';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import cs from 'classnames';
var searchUrl = "https://www.google.com.au/search?q=site:ssw.com.au%20";

var Menu = function Menu(_ref) {
  var onClickToggle = _ref.onClickToggle;

  var search = function search(_search) {
    if (window) {
      window.location.href = searchUrl + _search;
    }
  };

  var handleKeyDown = function handleKeyDown(event) {
    if (event.key === 'Enter') {
      search(event.target.value);
    }
  };

  return /*#__PURE__*/React.createElement("div", {
    className: styles.MegaMenu
  }, /*#__PURE__*/React.createElement("div", {
    className: styles.menuContent
  }, /*#__PURE__*/React.createElement("div", {
    className: cs(styles.menuMobile, styles.visibleXs, styles.visibleSm)
  }, /*#__PURE__*/React.createElement("div", {
    className: styles.sbToggleLeft,
    onClick: function onClick() {
      return onClickToggle();
    }
  }, /*#__PURE__*/React.createElement(FontAwesomeIcon, {
    icon: faBars
  }))), /*#__PURE__*/React.createElement(DesktopMenu, null), /*#__PURE__*/React.createElement("div", {
    className: styles.menuSearch
  }, /*#__PURE__*/React.createElement("input", {
    type: "text",
    className: styles.searchBox,
    onKeyDown: function onKeyDown(event) {
      return handleKeyDown(event);
    }
  }))));
};

export default Menu;