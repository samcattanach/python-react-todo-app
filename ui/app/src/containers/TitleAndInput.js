import React from "react";
import { Text, Input, Button, Flex, useColorMode } from "@chakra-ui/core";
import { connect } from "react-redux";

import * as actionTypes from "./../store/actions";

const TitleAndInput = (props) => {
  const { colorMode } = useColorMode();
  const buttonColorModeStyling = {
    light: {
      backgroundColor: "cyan.200",
      _hover: { backgroundColor: "blue.400" },
      _active: { backgroundColor: "blue.200" },
      _focus: { boxShadow: "0 0 0 2px #a3e0ea" },
    },
    dark: {
      backgroundColor: "gray.600",
      _hover: { backgroundColor: "gray.700" },
      _active: { backgroundColor: "gray.400" },
      _focus: { boxShadow: "0 0 0 2px #00A3C4" },
    },
  };

  const onKeyPress = (e) => {
    if (e.which === 13) {
      props.onAddTask();
    }
  };

  return (
    <div>
      <b>
        <Text
          color={colorMode === "light" ? "white.700" : "white.100"}
          fontSize={["4xl", "4xl", "4xl", "3xl"]}
          fontFamily="Trebuchet MS"
          margin="8px"
        >
          To-Do List
        </Text>
      </b>
      <Flex
        flexDirection="row"
        width={["calc(100% - 14px)", "85%"]}
        margin="0 auto"
        position="relative"
        right="4px"
      >
        <Input
          placeholder="Enter a new task..."
          backgroundColor={colorMode === "light" ? "white" : "white.100"}
          borderColor="white.200"
          color="white.700"
          focusBorderColor={colorMode === "light" ? "cyan.200" : "cyan.700"}
          margin="8px 1px"
          fontSize={["xl", "lg", "lg", "md"]}
          position="relative"
          left="4px"
          value={props.newText}
          onChange={(event) => props.onEnterNewTaskText(event.target.value)}
          onKeyPress={onKeyPress}
          _placeholder={{
            color: colorMode === "light" ? "white.400" : "white.500",
            fontSize: ["xl", "lg", "lg", "md"],
          }}
        />
        <Button
          color="white"
          margin="8px 1px"
          fontSize={["xl", "lg", "lg", "md"]}
          position="relative"
          left="4px"
          onClick={props.onAddTask}
          {...buttonColorModeStyling[colorMode]}
        >
          Add Task
        </Button>
      </Flex>
      <hr
        style={{
          borderWidth: "1px",
          margin: "8px",
          marginBottom: "10px",
          borderColor: colorMode === "light" ? "#d2eef3" : "#4A5568",
        }}
      />
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    newText: state.newTaskText,
    allList: state.allTaskList,
    visibleList: state.visibleTaskList,
  };
};

const mapDispatchToProps = (dispatch) => {
  return {
    onEnterNewTaskText: (text) =>
      dispatch({ type: actionTypes.ENTER_NEW_TASK_TEXT, newText: text }),
    onAddTask: () => dispatch({ type: actionTypes.ADD_TASK }),
  };
};

export default connect(mapStateToProps, mapDispatchToProps)(TitleAndInput);
