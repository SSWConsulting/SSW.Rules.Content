import _classCallCheck from "@babel/runtime/helpers/esm/classCallCheck";
import _createClass from "@babel/runtime/helpers/esm/createClass";
import _inherits from "@babel/runtime/helpers/esm/inherits";
import _createSuper from "@babel/runtime/helpers/esm/createSuper";
import React, { Suspense } from 'react';
import styles from './desktop-menu.module.css';
import cs from 'classnames';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleDown } from '@fortawesome/free-solid-svg-icons';
import MenuPanel from '../menu-panel/menu-panel';

var DesktopMenu = /*#__PURE__*/function (_React$Component) {
  _inherits(DesktopMenu, _React$Component);

  var _super = _createSuper(DesktopMenu);

  function DesktopMenu() {
    _classCallCheck(this, DesktopMenu);

    return _super.apply(this, arguments);
  }

  _createClass(DesktopMenu, [{
    key: "getRootUrl",
    value: function getRootUrl() {
      if (this.props.prefix && typeof window !== 'undefined') {
        return (window.location.origin ? window.location.origin + '/' : window.location.protocol + '/' + window.location.host + '/') + this.props.prefix + '/';
      }

      return '';
    }
  }, {
    key: "render",
    value: function render() {
      var _this = this;

      return /*#__PURE__*/React.createElement("div", {
        className: cs(styles.menuDrop, styles.hiddenXs, styles.hiddenSm)
      }, /*#__PURE__*/React.createElement("ul", null, this.props.menuModel && this.props.menuModel.menuItems.map(function (item, index) {
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
        }, /*#__PURE__*/React.createElement(MenuPanel, {
          item: item,
          prefix: _this.props.prefix
        }))));
      })));
    }
  }]);

  return DesktopMenu;
}(React.Component);

;
export default DesktopMenu;