import _classCallCheck from "@babel/runtime/helpers/esm/classCallCheck";
import _createClass from "@babel/runtime/helpers/esm/createClass";
import _inherits from "@babel/runtime/helpers/esm/inherits";
import _createSuper from "@babel/runtime/helpers/esm/createSuper";
import React from 'react';
import styles from './desktop-menu.module.css';
import cs from 'classnames';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleDown } from '@fortawesome/free-solid-svg-icons';
import Dropdown from '../dropdown/dropdown';
import axios from 'axios';

var DesktopMenu = /*#__PURE__*/function (_React$Component) {
  _inherits(DesktopMenu, _React$Component);

  var _super = _createSuper(DesktopMenu);

  //const DesktopMenu = ({prefix}) => {
  function DesktopMenu(props) {
    var _this;

    _classCallCheck(this, DesktopMenu);

    _this = _super.call(this, props);
    _this.state = {
      menuModel: null
    };
    return _this;
  }

  _createClass(DesktopMenu, [{
    key: "loadMenuModel",
    value: function loadMenuModel() {
      var currentComponent = this;
      axios.get('https://SSWConsulting.github.io/SSW.Website.Menu.json/menu.json').then(function (response) {
        currentComponent.setState({
          menuModel: response.data
        });
      }).catch(function (error) {
        console.log(error);
      });
    }
  }, {
    key: "componentDidMount",
    value: function componentDidMount() {
      this.loadMenuModel();
    }
  }, {
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
      var _this2 = this;

      return /*#__PURE__*/React.createElement("div", {
        className: cs(styles.menuDrop, styles.hiddenXs, styles.hiddenSm)
      }, /*#__PURE__*/React.createElement("ul", null, this.state.menuModel && this.state.menuModel.menuItems.map(function (item, index) {
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
          src: _this2.getRootUrl() + require("../images/" + item.groupImageUrl),
          loading: "lazy"
        })), /*#__PURE__*/React.createElement(Dropdown, {
          items: item.children
        }))));
      })));
    }
  }]);

  return DesktopMenu;
}(React.Component);

;
export default DesktopMenu;