package com.github.pawelwilkosz;

public class Main {
    public static void main(String[] argc) throws InterruptedException {
        ServiceBusWrapper serviceBusSender = new ServiceBusWrapper();
        ServiceBusWrapper serviceBusReceiver = new ServiceBusWrapper();

        serviceBusSender.sendMessage("Hello World to Azure!");
        serviceBusReceiver.receiveMessage();
    }
}
