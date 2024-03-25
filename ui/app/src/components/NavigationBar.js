import React from "react";
import { IconButton, Button, Flex, useColorMode } from "@chakra-ui/core";
import { GoMarkGithub } from "react-icons/go";
import { FaSun } from "react-icons/fa";

const NavigationBar = () => {
  const { colorMode, toggleColorMode } = useColorMode();

  return (
    <Flex
      flexDirection="row"
      backgroundColor={[
        colorMode === "light" ? "cyan.2000" : "transparent",
        "transparent",
      ]}
      border="4px solid"
      borderColor={[
        colorMode === "light" ? "transparent" : "white.600",
        "transparent",
      ]}
      borderBottomColor="transparent"
      textAlign="right"
      width="100%"
      padding={["2px", "6px"]}
      position="relative"
      zIndex="999"
    >
      <Button
        backgroundColor={colorMode === "light" ? "cyan.300" : "cyan.700"}
        color="white"
        leftIcon={colorMode === "light" ? "moon" : FaSun}
        size="sm"
        marginLeft="auto"
        zIndex="999"
        onClick={toggleColorMode}
        _hover={{
          backgroundColor: colorMode === "light" ? "cyan.400" : "cyan.800",
        }}
        _active={{
          backgroundColor: colorMode === "light" ? "cyan.200" : "cyan.2000",
        }}
        _focus={{
          boxShadow:
            colorMode === "light" ? "0 0 0 2px white" : "0 0 0 2px #00A3C4",
        }}
      >
        {colorMode === "" ? "" : ""} 
      </Button>
    </Flex>
  );
};

export default NavigationBar;
