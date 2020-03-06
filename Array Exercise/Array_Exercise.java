package com.company;
import java.util.*;
import java.util.stream.*;
import java.util.Scanner;



class Array_Exercise {
    // no.1
    public static void main(String[] args) {
        boolean test = false;
        Scanner sc = new Scanner(System.in);
        // input user and put them in array

        int[] arr = new int[20];
        for (int i = 0; i < 20; i++) {
            System.out.print("Enter a number: ");
            arr[i] = sc.nextInt();
        }

        // print the array
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i]);
        }
        // no.3
        System.out.println("\nFor no.3");
        int positive_total = 0;
        int negative_total = 0;
        int odd = 0;
        int even = 0;
        int zero = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > 0 && arr[i] % 2 != 0) {
                positive_total += 1;
                odd += 1;
            } else if (arr[i] > 0 && arr[i] % 2 == 0) {
                positive_total += 1;
                even += 1;
            } else if (arr[i] < 0 && arr[i] % 2 != 0) {
                odd += 1;
                negative_total += 1;
            } else if (arr[i] < 0 && arr[i] % 2 == 0) {
                even += 1;
                negative_total += 1;
            } else if (arr[i] == 0) {
                zero += 1;
            }
        }
        System.out.println("\nNumber of positive : " + positive_total);
        System.out.println("Number of negatives : " + negative_total);
        System.out.println("Number of odds : " + odd);
        System.out.println("Number of even : " + even);
        System.out.println("Number of 0 : " + zero);

        // no.4 and 5
        System.out.println("\nFor no 4 and 5");
        int min = arr[0];
        int max = arr[0];
        int sum_array = IntStream.of(arr).sum();
        int product_array = 1;

        for (int i = 0; i < arr.length; i++) {
            product_array = product_array * arr[i];
            if (arr[i] > max) {
                max = arr[i];
            }
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        System.out.println("Sum = " + sum_array);
        System.out.println("product = " + product_array);
        System.out.println("Min = " + min);
        System.out.println("Max = " + max);

        // no.2 guess
        System.out.println("\nFor no.2");
        for (int i = 0; i < arr.length; i++) {
            System.out.println("\nguess the number :");
            int guess_number = sc.nextInt();
            if (Arrays.asList(arr[i]).contains(guess_number)) {
                System.out.println("Number is in the array");
                break;
            } else {
                System.out.println("Number is not in array");
                break;
            }
        }

        //no.6
        System.out.println("\nFor no.6");
        int palindrome = 0;
        for (int i = 0; i <= arr.length / 2 && arr[i] != 0; i++) {
            // Check if first and last element are different
            // Then set flag to 1.
            if (arr[i] != arr[arr.length - i - 1]) {
                palindrome = 1;
                break;
            }
        }
        if (palindrome == 1) {
            System.out.println("Array is Not palindrome!");
        } else {
            System.out.println("Array is Palindrome!");
        }

        // no.7
        System.out.println("\nFor no.7");
        int[] Array = new int[10];
        Random rd = new Random(); // creating Random object
        for (int i = 0; i < 10; i++) {
            Array[i] = rd.nextInt(15);
        }
        System.out.println("Array before split :" + Arrays.toString(Array));
        int[] first_arr = Arrays.copyOfRange(Array, 0, Array.length / 2);
        int[] sec_arr = Arrays.copyOfRange(Array, Array.length / 2, Array.length);
        System.out.println("First half : " + Arrays.toString(first_arr));
        System.out.println("second half: " + Arrays.toString(sec_arr));

        // no.9
        System.out.println("\nFor no.9");
        int temp = 0;
        int[] array = {1, 2, 3, 4, 5};
        System.out.println("Original array :");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        temp = array[array.length - 1];
        for (int i = array.length - 1; i > 0; i--) {
            array[i] = array[i - 1];
        }
        array[0] = temp;
        System.out.println("\nAfter shift to the right :");
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }

        //no.10
        System.out.println("\nFor no.10");
        int[] array10 = {5, 4, 3, 2, 1};
        System.out.println("Before sorted :");
        for (int i = 0; i < array10.length; i++) {
            System.out.print(array10[i]+" ");
        }
        System.out.println("\nAfter sorted(Ascending) : ");
        Arrays.sort(array10);
        for (int i = 0; i < array10.length; i++) {
            System.out.print((array10[i]+" "));
        }
        //no.8
        System.out.println("\nFor no.8");
        int[] array8 = {4, 8, 6, 3, 2};
        int[] a = new int[array8.length + 1];
        System.out.println("Original array :");
        for (int i_8 = 0; i_8 < array8.length; i_8++) {
            a[i_8] = array8[i_8];
            System.out.print(a[i_8] + " ");
        }
        int max8 = a[0];
        int min8 = a[0];
        for (int i_8 = 0; i_8 < array8.length; i_8++) {
            if (a[i_8] > max8) {
                max8 = a[i_8];
            }
            if (a[i_8] < min8) {
                min8 = a[i_8];
            }
        }
        int next_max8 = 0;
        for (int k_8 = 0; k_8 < array8.length; k_8++) {
            if (a[k_8] < max8) {
                next_max8 = a[k_8];
                break;
            }
        }
        for (int i_8 = 0; i_8 < array8.length; i_8++) {
            if (a[i_8] > next_max8 && a[i_8] < max8) {
                next_max8 = a[i_8];


                int y = max8 - next_max8;
                int z = next_max8;
                System.out.println("\nAfter modified: ");
                for (int i_82 = 0; i_82 < array8.length + 1; i_82++) {
                    int new_z = array8.length;
                    if (a[i_82] != max8) {
                        System.out.print(a[i_82] + " ");
                    } else {
                        a[i_82] = z;
                        System.out.print(a[i_82] + " ");
                        while (new_z > i_82) {
                            a[new_z] = a[new_z - 1];
                            new_z--;
                        }
                        a[i_82 + 1] = y;
                        System.out.print(a[i_82 + 1] + " ");
                        i_82++;
                    }
                }
            }
        }
    }
}