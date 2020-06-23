import React from 'react';
import styles from './menu-panel.module.css';
import Dropdown from '../dropdown/dropdown';

var MenuPanel = function MenuPanel(_ref) {
  var item = _ref.item,
      prefix = _ref.prefix;

  var getRootUrl = function getRootUrl() {
    if (prefix && typeof window !== 'undefined') {
      return (window.location.origin ? window.location.origin + '/' : window.location.protocol + '/' + window.location.host + '/') + prefix + '/';
    }

    return '';
  };

  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("div", {
    className: styles.MenuImg
  }, /*#__PURE__*/React.createElement("img", {
    src: getRootUrl() + require("../images/" + item.groupImageUrl),
    alt: item.text,
    loading: "eager"
  })), /*#__PURE__*/React.createElement(Dropdown, {
    items: item.children
  }));
};

export default MenuPanel;