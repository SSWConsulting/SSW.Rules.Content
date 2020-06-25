import _createForOfIteratorHelper from "@babel/runtime/helpers/esm/createForOfIteratorHelper";
import _classCallCheck from "@babel/runtime/helpers/esm/classCallCheck";
import _createClass from "@babel/runtime/helpers/esm/createClass";
import _inherits from "@babel/runtime/helpers/esm/inherits";
import _createSuper from "@babel/runtime/helpers/esm/createSuper";
import React, { useState, componentDidMount } from 'react';
import styles from './mobile-menu.module.css';
import cs from 'classnames';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleDown } from '@fortawesome/free-solid-svg-icons';
import MobileDropdownItem from '../mobile-dropdown-item/mobile-dropdown-item';
import axios from 'axios';

var MobileMenu = /*#__PURE__*/function (_React$Component) {
  _inherits(MobileMenu, _React$Component);

  var _super = _createSuper(MobileMenu);

  //const DesktopMenu = ({prefix}) => {
  function MobileMenu(props) {
    var _this;

    _classCallCheck(this, MobileMenu);

    _this = _super.call(this, props);
    _this.state = {
      menuModel: null
    };
    return _this;
  }

  _createClass(MobileMenu, [{
    key: "loadMenuModel",
    value: function loadMenuModel() {
      if (!this.state.menuModel) {
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
    key: "closeOpenedElements",
    value: function closeOpenedElements() {
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
    }
  }, {
    key: "openElement",
    value: function openElement(element) {
      element.className = cs(styles.dropdown, styles.open);
    }
  }, {
    key: "closeElement",
    value: function closeElement(element) {
      element.className = styles.dropdown;
    }
  }, {
    key: "openItem",
    value: function openItem(event) {
      if (event.target.parentNode.className === styles.dropdown) {
        this.closeOpenedElements();
        this.openElement(event.target.parentNode);
      } else if (event.target.parentNode.parentNode.className === styles.dropdown) {
        this.closeOpenedElements();
        this.openElement(event.target.parentNode.parentNode);
      } else if (event.target.parentNode.className === cs(styles.dropdown, styles.open)) {
        this.closeElement(event.target.parentNode);
      } else if (event.target.parentNode.parentNode.className === cs(styles.dropdown, styles.open)) {
        this.closeElement(event.target.parentNode.parentNode);
      }
    }
  }, {
    key: "render",
    value: function render() {
      var _this2 = this;

      return /*#__PURE__*/React.createElement("div", {
        className: cs(styles.sbSlidebar, styles.sbLeft),
        style: {
          width: this.props.isMenuOpened ? '84vw' : '0px'
        },
        onClick: function onClick(event) {
          return _this2.openItem(event);
        }
      }, /*#__PURE__*/React.createElement("div", {
        className: cs(styles.menuDrop, styles.navbarCollapse)
      }, /*#__PURE__*/React.createElement("ul", {
        className: styles.navbarNav
      }, this.state.menuModel && this.state.menuModel.menuItems.map(function (item, index) {
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
    }
  }]);

  return MobileMenu;
}(React.Component);

;
export default MobileMenu;