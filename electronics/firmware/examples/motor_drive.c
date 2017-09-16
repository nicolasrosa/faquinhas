#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SLOTS "/sys/devices/bone_capemgr.9/slots"

#define DUTY_0 "/sys/devices/ocp.3/pwm_test_P9_14.16/duty"
#define PERIOD_0 "/sys/devices/ocp.3/pwm_test_P9_14.16/period"
#define POLARITY_0 "/sys/devices/ocp.3/pwm_test_P9_14.16/polarity"

#define DUTY_1 "/sys/devices/ocp.3/pwm_test_P9_21.15/duty"
#define PERIOD_1 "/sys/devices/ocp.3/pwm_test_P9_21.15/period"
#define POLARITY_1 "/sys/devices/ocp.3/pwm_test_P9_21.15/polarity"

#define DUTY_2 "/sys/devices/ocp.3/pwm_test_P8_19.17/duty"
#define PERIOD_2 "/sys/devices/ocp.3/pwm_test_P8_19.17/period"
#define POLARITY_2 "/sys/devices/ocp.3/pwm_test_P8_19.17/polarity"

#define DUTY_3 "/sys/devices/ocp.3/pwm_test_P9_42.18/duty"
#define PERIOD_3 "/sys/devices/ocp.3/pwm_test_P9_42.18/period"
#define POLARITY_3 "/sys/devices/ocp.3/pwm_test_P9_42.18/polarity"

#define PERIOD_PWM0 30000
#define PERIOD_PWM1 30000
#define PERIOD_PWM2 30000
#define PERIOD_PWM3 30000

void config_polarity(int); //Configura a polaridade do Duty Cicle,indicando o tempo em Alto
void config_period(int);
void config_duty(int,int);
void setting_speed(float,float,float,float);
//setting_speed.exe 0.3 0.5
//php exec(setting_speed.exe $speed1 $speed2);
int main(int argc,char *argv[]){
    float duty_motor1_arg1,duty_motor2_arg2,duty_motor3_arg3,duty_motor4_arg4;

    duty_motor1_arg1 = atof(argv[1]);
    duty_motor2_arg2 = atof(argv[2]);
    duty_motor3_arg3 = atof(argv[3]);
    duty_motor4_arg4 = atof(argv[4]);

    setting_speed(duty_motor1_arg1,duty_motor2_arg2,duty_motor3_arg3,duty_motor4_arg4);

return 0;
}

void setting_speed(float duty_m0,float duty_m1,float duty_m2,float duty_m3){
    int DUTY0, DUTY1, DUTY2, DUTY3;

    DUTY0 = 0.01*duty_m0*PERIOD_PWM0;
    DUTY1 = 0.01*duty_m1*PERIOD_PWM1;
    DUTY2 = 0.01*duty_m2*PERIOD_PWM2;
    DUTY3 = 0.01*duty_m3*PERIOD_PWM3;

    //setting_motor0
    config_polarity(0);
    config_period(0);
    config_duty(0,DUTY0);
    //setting_motor1
    config_polarity(1);
    config_period(1);
    config_duty(1,DUTY1);
    //setting_motor2
    config_polarity(2);
    config_period(2);
    config_duty(2,DUTY2);
    //setting_motor3
    config_polarity(3);
    config_period(3);
    config_duty(3,DUTY3);

}

void config_polarity(int id_motor){
    FILE *arquivo;

    if(id_motor==0){
        if((arquivo = fopen(POLARITY_0,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(POLARITY_0,"w");
            fprintf(arquivo,"0");
            fclose(arquivo);
        }
    }

    if(id_motor==1){
        if((arquivo = fopen(POLARITY_1,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(POLARITY_1,"w");
            fprintf(arquivo,"0");
            fclose(arquivo);
        }
    }
    if(id_motor==2){
        if((arquivo = fopen(POLARITY_2,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(POLARITY_2,"w");
            fprintf(arquivo,"0");
            fclose(arquivo);
        }
    }

    if(id_motor==3){
        if((arquivo = fopen(POLARITY_3,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(POLARITY_3,"w");
            fprintf(arquivo,"0");
            fclose(arquivo);
        }
    }

}

void config_period(int id_motor){
    FILE *arquivo;

    if(id_motor==0){
        if((arquivo = fopen(PERIOD_0,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(PERIOD_0,"w");
            fprintf(arquivo,"%d",PERIOD_PWM0);
            fclose(arquivo);
        }
    }

    if(id_motor==1){
        if((arquivo = fopen(PERIOD_1,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(PERIOD_1,"w");
            fprintf(arquivo,"%d",PERIOD_PWM1);
            fclose(arquivo);
        }
    }

    if(id_motor==2){
        if((arquivo = fopen(PERIOD_2,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(PERIOD_2,"w");
            fprintf(arquivo,"%d",PERIOD_PWM2);
            fclose(arquivo);
        }
    }

    if(id_motor==3){
        if((arquivo = fopen(PERIOD_3,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(PERIOD_3,"w");
            fprintf(arquivo,"%d",PERIOD_PWM3);
            fclose(arquivo);
        }
    }

    printf("Period Ok...\n");
}

void config_duty(int id_motor,int valor_duty){
    FILE *arquivo;

    if(id_motor==0){
        if((arquivo = fopen(DUTY_0,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(DUTY_0,"w");
            fprintf(arquivo,"%d",valor_duty);
            fclose(arquivo);
        }
    }

    if(id_motor==1){
        if((arquivo = fopen(DUTY_1,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(DUTY_1,"w");
            fprintf(arquivo,"%d",valor_duty);
            fclose(arquivo);
        }
    }

    if(id_motor==2){
        if((arquivo = fopen(DUTY_2,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(DUTY_2,"w");
            fprintf(arquivo,"%d",valor_duty);
            fclose(arquivo);
        }
    }

    if(id_motor==3){
        if((arquivo = fopen(DUTY_3,"w")) == NULL){
                printf("Erro ao abrir arquivo!!!\n");
                exit(1);
        }else{
            arquivo = fopen(DUTY_3,"w");
            fprintf(arquivo,"%d",valor_duty);
            fclose(arquivo);
        }
    }

    printf("Duty Ok...\n");
}
