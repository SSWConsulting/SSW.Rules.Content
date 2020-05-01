import _createForOfIteratorHelper from "@babel/runtime/helpers/esm/createForOfIteratorHelper";
import React from 'react';
import styles from './mobile-menu.module.css';
import cs from 'classnames';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleDown } from '@fortawesome/free-solid-svg-icons';
import MobileDropdownItem from '../mobile-dropdown-item/mobile-dropdown-item';

var menuModel = require('../data/menu.json');

var MobileMenu = function MobileMenu(_ref) {
  var isMenuOpened = _ref.isMenuOpened;

  var closeOpenedElements = function closeOpenedElements() {
    var openedItems = document.getElementsByClassName(cs(styles.dropdown, styles.open));

    var _iterator = _createForOfIteratorHelper(openedItems),
        _step;

    try {
      for (_iterator.s(); !(_step = _iterator.n()).done;) {
        var item = _step.value;
        item.className = styles.dropdown;
      }
    } catch (err) {
      _iterator.e(err);
    } finally {
      _iterator.f();
    }
  };

  var openElement = function openElement(element) {
    element.className = cs(styles.dropdown, styles.open);
  };

  var closeElement = function closeElement(element) {
    element.className = styles.dropdown;
  };

  var openItem = function openItem(event) {
    if (event.target.parentNode.className === styles.dropdown) {
      closeOpenedElements();
      openElement(event.target.parentNode);
    } else if (event.target.parentNode.parentNode.className === styles.dropdown) {
      closeOpenedElements();
      openElement(event.target.parentNode.parentNode);
    } else if (event.target.parentNode.className === cs(styles.dropdown, styles.open)) {
      closeElement(event.target.parentNode);
    } else if (event.target.parentNode.parentNode.className === cs(styles.dropdown, styles.open)) {
      closeElement(event.target.parentNode.parentNode);
    }
  };

  return /*#__PURE__*/React.createElement("div", {
    className: cs(styles.sbSlidebar, styles.sbLeft),
    style: {
      width: isMenuOpened ? '84vw' : '0px'
    },
    onClick: function onClick(event) {
      return openItem(event);
    }
  }, /*#__PURE__*/React.createElement("div", {
    className: cs(styles.menuDrop, styles.navbarCollapse)
  }, /*#__PURE__*/React.createElement("ul", {
    className: styles.navbarNav
  }, menuModel.menuItems.map(function (item, index) {
    if (!item.children) {
      return /*#__PURE__*/React.createElement("li", {
        key: index,
        className: styles.dropdown
      }, /*#__PURE__*/React.createElement("a", {
        href: item.navigateUrl,
        className: cs(styles.ignore, 'unstyled')
      }, item.text));
    } else if (item.children) {
      return /*#__PURE__*/React.createElement("li", {
        key: index,
        className: styles.dropdown
      }, /*#__PURE__*/React.createElement("a", {
        className: cs(styles.dropdownToggle, 'unstyled')
      }, item.text, " ", /*#__PURE__*/React.createElement(FontAwesomeIcon, {
        icon: faAngleDown
      })), /*#__PURE__*/React.createElement("ul", {
        className: styles.dropdownMenu
      }, item.children.map(function (level1Item, indexLevel1) {
        return /*#__PURE__*/React.createElement(MobileDropdownItem, {
          key: indexLevel1,
          item: level1Item
        });
      })));
    }
  }))));
};

export default MobileMenu;