import React from "react";
import { connect } from "react-redux";
import { Button, Flex, useColorMode } from "@chakra-ui/core";
import { FaListUl } from "react-icons/fa";

import * as actionTypes from "./../store/actions";

const CategoryButtons = (props) => {
  const { colorMode } = useColorMode();
  const bgColor = { light: "cyan.200", dark: "gray.600" };
  const selectedBgColor = { light: "cyan.300", dark: "cyan.700" };
  const hoverColor = { light: "blue.400", dark: "gray.700" };
  const selectedHoverColor = { light: "cyan.400", dark: "cyan.800" };
  const activeColor = { light: "blue.200", dark: "gray.400" };
  const selectedActiveColor = { light: "cyan.200", dark: "cyan.2000" };

  return (
    <Flex
      flexDirection="row"
      width="100%"
      margin="2px auto 6px auto"
      justifyContent="center"
      position="relative"
      left={["0", "4px"]}
    >
      <Button
        backgroundColor={
          props.currentCol === "to do"
            ? selectedBgColor[colorMode]
            : bgColor[colorMode]
        }
        color="white"
        width="33%"
        margin={["2px 1px", "2px"]}
        fontSize={["xl", "lg", "lg", "md"]}
        leftIcon="calendar"
        onClick={props.onClickToDo}
        _hover={{
          backgroundColor:
            props.currentCol === "to do"
              ? selectedHoverColor[colorMode]
              : hoverColor[colorMode],
        }}
        _active={{
          backgroundColor:
            props.currentCol === "to do"
              ? selectedActiveColor[colorMode]
              : activeColor[colorMode],
        }}
        _focus={{
          boxShadow:
            colorMode === "light" ? "0 0 0 2px gray" : "0 0 0 2px #00A3C4",
        }}
      >
        To Do
      </Button>
      <Button
        backgroundColor={
          props.currentCol === "done"
            ? selectedBgColor[colorMode]
            : bgColor[colorMode]
        }
        color="white"
        width="33%"
        margin={["2px 1px", "2px"]}
        fontSize={["xl", "lg", "lg", "md"]}
        leftIcon="check-circle"
        onClick={props.onClickDone}
        _hover={{
          backgroundColor:
            props.currentCol === "done"
              ? selectedHoverColor[colorMode]
              : hoverColor[colorMode],
        }}
        _active={{
          backgroundColor:
            props.currentCol === "done"
              ? selectedActiveColor[colorMode]
              : activeColor[colorMode],
        }}
        _focus={{
          boxShadow:
            colorMode === "light" ? "0 0 0 2px white" : "0 0 0 2px #00A3C4",
        }}
      >
        Done
      </Button>
      <Button
        backgroundColor={
          props.currentCol === "all"
            ? selectedBgColor[colorMode]
            : bgColor[colorMode]
        }
        color="white"
        width="33%"
        margin={["2px 1px", "2px"]}
        fontSize={["xl", "lg", "lg", "md"]}
        leftIcon={FaListUl}
        onClick={props.onClickAll}
        _hover={{
          backgroundColor:
            props.currentCol === "all"
              ? selectedHoverColor[colorMode]
              : hoverColor[colorMode],
        }}
        _active={{
          backgroundColor:
            props.currentCol === "all"
              ? selectedActiveColor[colorMode]
              : activeColor[colorMode],
        }}
        _focus={{
          boxShadow:
            colorMode === "light" ? "0 0 0 2px gray" : "0 0 0 2px #00A3C4",
        }}
      >
        All Tasks
      </Button>
    </Flex>
  );
};

const mapStateToProps = (state) => {
  return {
    currentCol: state.currentColumn,
    list: state.allTaskList,
    visibleList: state.visibleTaskList,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    onClickToDo: () => dispatch({ type: actionTypes.CLICK_TO_DO }),
    onClickDone: () => dispatch({ type: actionTypes.CLICK_DONE }),
    onClickAll: () => dispatch({ type: actionTypes.CLICK_ALL }),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(CategoryButtons);
