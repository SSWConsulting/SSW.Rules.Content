import _classCallCheck from "@babel/runtime/helpers/esm/classCallCheck";
import _createClass from "@babel/runtime/helpers/esm/createClass";
import _inherits from "@babel/runtime/helpers/esm/inherits";
import _createSuper from "@babel/runtime/helpers/esm/createSuper";
import React from 'react';
import styles from './menu.module.css';
import DesktopMenu from '../desktop-menu/desktop-menu';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars } from '@fortawesome/free-solid-svg-icons';
import cs from 'classnames';
import axios from 'axios';
var searchUrl = "https://www.google.com.au/search?q=site:ssw.com.au%20";

var menuModel = require('../data/menu.json'); //const Menu = ({ onClickToggle, prefix }) => {


var Menu = /*#__PURE__*/function (_React$Component) {
  _inherits(Menu, _React$Component);

  var _super = _createSuper(Menu);

  //const DesktopMenu = ({prefix}) => {
  function Menu(props) {
    var _this;

    _classCallCheck(this, Menu);

    _this = _super.call(this, props);
    _this.state = {
      menuModel: menuModel
    };
    return _this;
  }

  _createClass(Menu, [{
    key: "loadMenuModel",
    value: function loadMenuModel() {
      if (this.state.menuModel === menuModel) {
        var currentComponent = this;
        axios.get('https://SSWConsulting.github.io/SSW.Website.Menu.json/menu.json').then(function (response) {
          currentComponent.setState({
            menuModel: response.data
          });
        }).catch(function (error) {
          console.log(error);
        });
      }
    }
  }, {
    key: "componentDidMount",
    value: function componentDidMount() {
      this.loadMenuModel();
    }
  }, {
    key: "menu_Search",
    value: function menu_Search(search) {
      if (window) {
        window.open(searchUrl + search);
      }
    }
  }, {
    key: "handleKeyDownOnMenuSearchInput",
    value: function handleKeyDownOnMenuSearchInput(event) {
      if (event.key === 'Enter') {
        this.menu_Search(event.target.value);
      }
    }
  }, {
    key: "render",
    value: function render() {
      var _this2 = this;

      return (
        /*#__PURE__*/
        // this.state.menuModel &&
        React.createElement("div", {
          className: styles.MegaMenu
        }, /*#__PURE__*/React.createElement("div", {
          className: styles.menuContent
        }, /*#__PURE__*/React.createElement("div", {
          className: cs(styles.menuMobile, styles.visibleXs, styles.visibleSm)
        }, /*#__PURE__*/React.createElement("div", {
          className: styles.sbToggleLeft,
          onClick: function onClick() {
            return _this2.props.onClickToggle();
          }
        }, /*#__PURE__*/React.createElement(FontAwesomeIcon, {
          icon: faBars
        }))), /*#__PURE__*/React.createElement(DesktopMenu, {
          prefix: this.props.prefix,
          menuModel: this.state.menuModel
        }), /*#__PURE__*/React.createElement("div", {
          className: styles.menuSearch
        }, /*#__PURE__*/React.createElement("input", {
          type: "text",
          className: styles.searchBox,
          onKeyDown: function onKeyDown(event) {
            return _this2.handleKeyDownOnMenuSearchInput(event);
          }
        }))))
      );
    }
  }]);

  return Menu;
}(React.Component);

export default Menu;