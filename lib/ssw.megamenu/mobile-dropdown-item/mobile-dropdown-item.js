import React from 'react';
import styles from './mobile-dropdown-item.module.css';

var MobileDropdownItem = function MobileDropdownItem(_ref) {
  var item = _ref.item,
      index = _ref.index;
  return /*#__PURE__*/React.createElement(React.Fragment, null, /*#__PURE__*/React.createElement("li", {
    key: index,
    className: styles.level1
  }, /*#__PURE__*/React.createElement("a", {
    href: item.navigateUrl,
    className: styles.ignore
  }, item.text)));
};

export default MobileDropdownItem;