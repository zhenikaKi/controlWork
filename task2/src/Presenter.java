package src;

import java.io.FileWriter;
import java.util.Scanner;

/** Обработка работы магазина */
public class Presenter {

    /** Имя файла для итогов работы магазина */
    private final static String FILE_NAME = "task2/output.txt";

    private final static int CMD_EXIT = 0;
    private final static int CMD_GET_TOY = 1;
    private final static int CMD_CHANGE_WEIGHT = 2;
    private final static int CMD_TOYS = 3;
    private final static int CMD_ADD_TOY = 4;

    private final ToyShop toyShop = new ToyShop();
    private final Scanner scanner = new Scanner(System.in, "Cp866");

    public Presenter() {
        //создаем файл под результат работы магазина
        try(FileWriter fileWriter = new FileWriter(FILE_NAME, false)) {
            fileWriter.flush();
        }
        catch (Exception e) {
            throw new RuntimeException("Возникла ошибка при работе с результирующим файлом", e);
        }
    }

    /** Запустить работу магазина */
    public void runShop() {
        while (true) {
            try {
                if (processCmd(getUserCommand())) {
                    break;
                }
            }
            catch (Exception e) {
                System.err.println("Возникла ошибка: " + e.getMessage());
            }
        }
    }

    /**
     * Обработать команду пользователя.
     * @param cmd Введенная команда.
     * @return True - введена команды выхода, false - введена обычня команда.
     */
    private boolean processCmd(int cmd) {
        switch (cmd) {
            case CMD_EXIT:
                return true;
            case CMD_GET_TOY:
                System.out.println(toyShop.getToy());
                break;
            case CMD_CHANGE_WEIGHT:
                changeWeight();
                break;
            case CMD_TOYS:
                printToys();
                break;
            case CMD_ADD_TOY:
                addToy();
                break;
            default:
                new RuntimeException("Некорректная команда");
        }

        return false;
    }

    /** Добавить игрушку в магазин */
    private void addToy() {
        System.out.print("Введите id игрушки: ");
        int id = scanner.nextInt();
        System.out.print("Введите имя игрушки: ");
        String title = scanner.next();
        System.out.print("Введите вес: ");
        float weight = scanner.nextFloat();
        System.out.print("Введите количество игрушек: ");
        int count = scanner.nextInt();
        toyShop.addToy(id, title, weight, count);

    }

    /** Изменить вес игрушки */
    private void changeWeight() {
        System.out.print("Введите id игрушки: ");
        int id = scanner.nextInt();
        System.out.print("Введите новый вес: ");
        float weight = scanner.nextFloat();
        toyShop.changeWeight(id, weight);
    }

    /** Напечатать данные по игрушкам */
    private void printToys() {
        toyShop.getToysInfo().forEach(System.out::println);
    }

    /** Напечатать список команд и получить команду, которую ввел пользователь */
    private int getUserCommand() {
        System.out.println("----- Список команд -----");
        System.out.println(CMD_EXIT + " - выход");
        System.out.println(CMD_GET_TOY + " - получить игрушку");
        System.out.println(CMD_CHANGE_WEIGHT + " - изменить вес игрушки (по id)");
        System.out.println(CMD_TOYS + " - показать данные по игрушкам");
        System.out.println(CMD_ADD_TOY + " - добавить игрушку");
        System.out.print("Введите номер команды: ");
        return scanner.nextInt();
    }
}
