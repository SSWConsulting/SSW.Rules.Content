import React from 'react';
import styles from './desktop-menu.module.css';
import cs from 'classnames';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleDown } from '@fortawesome/free-solid-svg-icons';
import Dropdown from '../dropdown/dropdown';

var menuModel = require('../data/menu.json');

var DesktopMenu = function DesktopMenu() {
  return /*#__PURE__*/React.createElement("div", {
    className: cs(styles.menuDrop, styles.hiddenXs, styles.hiddenSm)
  }, /*#__PURE__*/React.createElement("ul", null, menuModel.menuItems.map(function (item, index) {
    return /*#__PURE__*/React.createElement("li", {
      key: index
    }, !item.children && /*#__PURE__*/React.createElement("a", {
      href: item.navigateUrl ? item.navigateUrl : null,
      className: cs(styles.ignore, 'unstyled')
    }, item.text), ' ', item.children && /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("a", {
      className: cs(styles.ignore, 'unstyled')
    }, item.text, " ", /*#__PURE__*/React.createElement(FontAwesomeIcon, {
      icon: faAngleDown
    })), /*#__PURE__*/React.createElement("div", {
      className: styles.Menu
    }, /*#__PURE__*/React.createElement("div", {
      className: styles.MenuImg
    }, /*#__PURE__*/React.createElement("img", {
      src: require("../images/" + item.groupImageUrl),
      loading: "lazy"
    })), /*#__PURE__*/React.createElement(Dropdown, {
      items: item.children
    }))));
  })));
};

export default DesktopMenu;