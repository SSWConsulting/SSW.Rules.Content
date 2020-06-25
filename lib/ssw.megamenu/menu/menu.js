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

var Menu = /*#__PURE__*/function (_React$Component) {
  _inherits(Menu, _React$Component);

  var _super = _createSuper(Menu);

  function Menu() {
    _classCallCheck(this, Menu);

    return _super.apply(this, arguments);
  }

  _createClass(Menu, [{
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
      var _this = this;

      var _this$props = this.props,
          menuModel = _this$props.menuModel,
          menuLoaded = _this$props.menuLoaded;
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
            return _this.props.onClickToggle();
          }
        }, /*#__PURE__*/React.createElement(FontAwesomeIcon, {
          icon: faBars
        }))), /*#__PURE__*/React.createElement(DesktopMenu, {
          prefix: this.props.prefix,
          menuModel: menuModel
        }), /*#__PURE__*/React.createElement("div", {
          className: styles.menuSearch
        }, /*#__PURE__*/React.createElement("input", {
          type: "text",
          className: styles.searchBox,
          onKeyDown: function onKeyDown(event) {
            return _this.handleKeyDownOnMenuSearchInput(event);
          }
        }))))
      );
    }
  }]);

  return Menu;
}(React.Component);

var Wrapper = /*#__PURE__*/function (_React$Component2) {
  _inherits(Wrapper, _React$Component2);

  var _super2 = _createSuper(Wrapper);

  function Wrapper(props) {
    var _this2;

    _classCallCheck(this, Wrapper);

    _this2 = _super2.call(this, props);
    _this2.state = {
      menuModel: require('../data/menu.json'),
      menuLoaded: false
    };
    return _this2;
  }

  _createClass(Wrapper, [{
    key: "componentDidMount",
    value: function componentDidMount() {
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
    key: "render",
    value: function render() {
      var _this$state = this.state,
          menuModel = _this$state.menuModel,
          menuLoaded = _this$state.menuLoaded;
      return /*#__PURE__*/React.createElement(Menu, Object.assign({
        menuModel: menuModel,
        menuLoaded: menuLoaded
      }, this.props));
    }
  }]);

  return Wrapper;
}(React.Component);

export default Wrapper;