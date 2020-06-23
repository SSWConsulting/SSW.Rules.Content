import React from 'react';
import styles from './dropdown-item.module.css';
import cs from 'classnames';

var DropdownItem = function DropdownItem(_ref) {
  var item = _ref.item,
      index = _ref.index;
  return /*#__PURE__*/React.createElement(React.Fragment, null, item.level === 1 && /*#__PURE__*/React.createElement("li", {
    key: index,
    className: item.data.navigateUrlOnMobileOnly ? item.data.cssClass ? cs(styles[item.data.cssClass], styles.NonClickableMenuItem, styles.level1) : cs(styles.NonClickableMenuItem, styles.level1) : item.data.cssClass ? cs(styles[item.data.cssClass], styles.level1) : styles.level1
  }, item.data.navigateUrlOnMobileOnly && /*#__PURE__*/React.createElement("span", {
    className: 'unstyled'
  }, item.data.text), !item.data.navigateUrlOnMobileOnly && /*#__PURE__*/React.createElement("a", {
    href: item.data.navigateUrl,
    className: 'unstyled'
  }, item.data.text)), item.level === 2 && /*#__PURE__*/React.createElement("li", {
    key: index,
    className: item.data.cssClass ? cs(styles[item.data.cssClass], styles.ClickableMenuItem, styles.level2) : cs(styles.ClickableMenuItem, styles.level2)
  }, /*#__PURE__*/React.createElement("a", {
    href: item.data.navigateUrl ? item.data.navigateUrl : null,
    className: 'unstyled'
  }, item.data.text)));
};

export default DropdownItem;