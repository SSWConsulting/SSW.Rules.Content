import React from 'react';
import DropdownItem from '../dropdown-item/dropdown-item';
import styles from './dropdown.module.css';

var Dropdown = function Dropdown(_ref) {
  var items = _ref.items;

  var CountChildren = function CountChildren(items) {
    var count = items.length;
    items.forEach(function (level1) {
      if (level1.children) {
        count += level1.children.length;
      }
    });
    return count;
  };

  var createDropDown = function createDropDown(items) {
    var blocks = [];
    blocks.push([]);
    var countChildren = CountChildren(items);
    var currentIndex = 0;
    var currentColumn = 0;
    items.forEach(function (level1Item) {
      if (level1Item.breakListBefore) {
        currentColumn++;
        currentIndex = 0;
        blocks.push([]);
      }

      blocks[currentColumn].push({
        level: 1,
        data: level1Item
      });

      if (level1Item.children) {
        level1Item.children.forEach(function (level2Item) {
          if (level2Item.breakListBefore) {
            currentIndex++;

            if (level2Item.breakListBefore || currentIndex > countChildren / currentColumn) {
              currentColumn++;
              currentIndex = 0;
              blocks.push([]);
            }
          }

          blocks[currentColumn].push({
            level: 2,
            data: level2Item
          });
        });
      }
    });
    return blocks.map(function (column, index) {
      return /*#__PURE__*/React.createElement("ul", {
        key: index,
        className: styles.colMd3
      }, column.map(function (item, index) {
        return /*#__PURE__*/React.createElement(DropdownItem, {
          key: index,
          item: item
        });
      }));
    });
  };

  return /*#__PURE__*/React.createElement("div", {
    className: styles.MenuWrapper
  }, createDropDown(items));
};

export default Dropdown;