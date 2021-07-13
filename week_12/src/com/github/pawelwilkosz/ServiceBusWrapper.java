package com.github.pawelwilkosz;

import com.azure.messaging.servicebus.*;

import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.Arrays;
import java.util.List;

public class ServiceBusWrapper {
    private final String connectionString = "<FILL>";
    private final String queueName = "<FILL>";

    public void sendMessage(String message){
        ServiceBusSenderClient client = new ServiceBusClientBuilder()
                .connectionString(connectionString)
                .sender()
                .queueName(queueName)
                .buildClient();
        client.sendMessage(new ServiceBusMessage(message));
        System.out.println("Message sent...");
    }

    public void receiveMessage() throws InterruptedException {
        CountDownLatch countdownLatch = new CountDownLatch(1);

        ServiceBusProcessorClient  processorClient = new ServiceBusClientBuilder()
                .connectionString(connectionString)
                .processor()
                .queueName(queueName)
                .processMessage(ServiceBusWrapper::processMessage)
                .processError(context -> processError(context, countdownLatch))
                .buildProcessorClient();

        processorClient.start();

        TimeUnit.SECONDS.sleep(10);
        processorClient.close();
    }

    private static void processMessage(ServiceBusReceivedMessageContext context) {
        ServiceBusReceivedMessage message = context.getMessage();
        System.out.println("Received from queue: " + message.getBody());

    }

    private static void processError(ServiceBusErrorContext serviceBusReceivedMessageContext,
                                     CountDownLatch countDownLatch) {
        // TODO implement
        System.out.println("An error occured");
    }
}
